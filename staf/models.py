from django.db import models
from random import shuffle
# Create your models here.
class Stafuser(models.Model):
    photo = models.ImageField()
    username=models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)


class Coustmer(models.Model):
    photo = models.ImageField(upload_to="profile")
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.EmailField(max_length=90,unique=True)
    mobile = models.CharField(max_length=15,unique=True)
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150,blank=True,null=True)
    pin = models.CharField(max_length=6)
    state = models.CharField(max_length=150)
    pan_card = models.CharField(max_length=12,unique=True)
    pan_photo = models.ImageField(upload_to="adharacard")
    addhar_card = models.CharField(max_length=12,unique=True)
    adhar_f = models.ImageField(upload_to="adharacard")
    adhar_b = models.ImageField(upload_to="adharacard")
    status = models.BooleanField(default=False)
    # addhar_data = models.JSONField(o)
    def __str__(self):
        return self.email



class AccountDetails(models.Model):
    account_no=models.CharField(max_length=16,unique=True,default="16711040000")
    coustmerid=models.CharField(max_length=8,unique=True,default="8658")
    balance = models.FloatField(default=2500)
    created_at=models.DateTimeField(auto_now_add=True)
    types=models.CharField(max_length=12,default="saving")
    Branch=models.CharField(max_length=30,default="kakatpur")
    ModeofOperation=models.CharField(max_length=30,default="Single")
    ifsc_code=models.CharField(max_length=12,default="fi0001671")
    coustmer = models.OneToOneField(Coustmer, on_delete=models.CASCADE,blank=True,null=True)
    status = models.BooleanField(default=False)
    mpin = models.CharField(max_length=4)
    creditCard = models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.account_no
    


class CreditCardDetails(models.Model):
    credit_card_no=models.IntegerField(unique=True)
    cvv=models.IntegerField()
    ex_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    coustmer1 = models.OneToOneField(AccountDetails, on_delete=models.CASCADE,blank=True,null=True)

class CoustmerOtp(models.Model):
    otp = models.CharField(max_length=4)
    coustmer = models.ForeignKey(Coustmer, on_delete=models.CASCADE,blank=True,null=True) 