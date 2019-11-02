from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    summary = models.TextField()
    status = models.CharField(max_length=64)
    start_date = models.DateField(default=now)
    tenure = models.IntegerField()
    rate_of_return = models.CharField(max_length=32)
    image_top_name = models.CharField(max_length=255, default="images/des_moines.png")
    minimum_investment = models.IntegerField(default=10000)
    project_address = models.CharField(max_length=255)
    financials = models.TextField()
    investors = models.IntegerField(default=0)       #The current number of investors for this project
    total_amount = models.IntegerField(default=0)
    committed_amount = models.IntegerField(default=0)     #The amount of funds currently commmitted to the project

    def __str__(self):
        return self.name


class ProjectStatusHistory(models.Model):
    project_id = models.ForeignKey(
        Project,
        on_delete=models.PROTECT
    )
    status = models.CharField(max_length=64)
    time_stamp = models.DateTimeField()


class Investor(models.Model):
    investor_id = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )
    tax_id = models.CharField(max_length=16)
    #projects_supported = models.ManyToManyField()
    committed_amount = models.FloatField(default=0)      #The amount that the investor has committed for investment (so far)
    kyc_complete = models.BooleanField()