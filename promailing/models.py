import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.utils.functional import cached_property

USER_MODEL = get_user_model()


class EmailVerificationCode(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    verification_code = models.PositiveIntegerField(unique=True, validators=[])
    created_on = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'verification_code'], name='one_code_per_user')
        ]

    def __str__(self):
        return str(self.verification_code)

    @cached_property
    def expiry_date(self):
        return self.created_on + datetime.timedelta(days=1)

    @cached_property
    def expired(self):
        return self.created_on > self.expiry_date
