# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.mail import EmailMultiAlternatives
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# serializers
from .profileserializer import ProfileSerializer

# Models
from users.models import User,Profile

# #tasks
# from users.tasks import add

# Utilities
import jwt
from datetime import timedelta

class UsersSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username','first_name','last_name','is_active','date_created','phone_number','profile','is_client','user_created']
        #exclude = ['date_joined']

class UsersLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=60)

    def validate(self, data):
        user= authenticate(username=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError('credentials invalid')
        if not user.is_verified:
            raise serializers.ValidationError('acount is not verified')
        self.context['user']=user
        return data
        
    def create(self, data):
        token , created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'],token.key

class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    user_created = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        Profile.objects.create(user=user)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """Send account verification link to given user."""
        verification_token = self.gen_verification_token(user)
        subject = 'Welcome @{}! Verify your account to start using test django rest frameworks '.format(user.username)
        from_email = 'test django rest frameworks  <noreply@test.com>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token': verification_token, 'user': user}
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

    def gen_verification_token(self, user):
        """Create JWT token that the user can use to verify its account."""
        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            'user': user.username,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

class UserVerificationSerializer(serializers.Serializer):
    token=serializers.CharField()

    def validate_token(self, data):
        try:
            payload= jwt.decode(data, settings.SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('verification link has expired')
        except jwt.PyJWTError:
            raise serializers.ValidationError('invalid token!')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('invalid token!!')
        self.context['payload'] = payload
        return data

    def save(self):
        payload =self.context['payload']
        user = User.objects.get(username=payload['user'])
        user.is_verified = True
        user.save()
        return payload