from django.db import models

class defaultModels(models.Model):
    """
    Docs.
    """
    is_activate = models.BooleanField(default=True)
    user_created = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_user_created_name",
        related_query_name="%(app_label)s_%(class)s_user_created_query",
        null=True,
        blank=True
    )
    date_created= models.DateField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the obejec was last created.',
    )
    user_modified = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_user_modified_name",
        related_query_name="%(app_label)s_%(class)s_user_modified_query",
        null=True,
        blank=True
        )
    date_modified= models.DateField(
        'modified at',
        help_text='Date time on which the obejec was last modified.',
        null=True
    )
    class Meta:
        """
        Docs.
        """
        abstract= True
        get_latest_by = 'date_created'
        ordering= ['date_created','date_modified']