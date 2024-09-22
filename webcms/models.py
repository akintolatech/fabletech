from django.db import models

# Create your models here.


class WebDetails (models.Model):
    logo_of_business = models.ImageField(upload_to="webcms", blank=True, null=True)
    name_of_business = models.CharField(max_length=33)
    phone_of_business = models.CharField(max_length=11)
    address_of_business = models.CharField(max_length=100)
    phrase_of_business = models.CharField(max_length=500)
    email_of_business = models.CharField(max_length=33)
    maplink = models.CharField(max_length=3000, blank=True)

    def __str__(self):
        return self.name_of_business
