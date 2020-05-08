from django.contrib.auth.models import User
from django.db import models


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    company_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.company_name:
            return "{} - ({})".format(self.company_name, self.user)
        #return "{} {}".format(self.name, self.last_name)

