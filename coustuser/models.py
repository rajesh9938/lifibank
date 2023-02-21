from django.db import models
from staf.models import AccountDetails
# Create your models here.
class Transactions(models.Model):
    transaction_no = models.CharField(max_length=8,unique=True)
    account = models.ForeignKey(AccountDetails, on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    amount = models.FloatField()
    withdraw_no = models.CharField(max_length=16,blank=True,null=True)
    status = models.BooleanField(blank=True,null=True)
    transaction_type = models.CharField(max_length=6,blank=True,null=True)
