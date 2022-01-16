from rest_framework.authentication import TokenAuthentication

class TokenAuthenticationBearer(TokenAuthentication):
    keyword = 'Bearer'