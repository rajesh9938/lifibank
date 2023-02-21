from django.contrib import admin
from .models import Stafuser,Coustmer,AccountDetails,CreditCardDetails,CoustmerOtp
# Register your models here.
@admin.register(Stafuser)
class adminuser(admin.ModelAdmin):
    list_display = ["username","name", "password"]

@admin.register(Coustmer)
class admincoustmer(admin.ModelAdmin):
    list_display=["id","photo","first_name","last_name","address","address2","pin","state","email","mobile","pan_card","pan_photo","addhar_card","adhar_f","adhar_b","status"]

@admin.register(AccountDetails)
class adminAccountDetails(admin.ModelAdmin):
    list_display=["balance","account_no","coustmerid","created_at","types","Branch","ModeofOperation","ifsc_code","status","coustmer","creditCard"]

@admin.register(CoustmerOtp)
class CoustmerOtp(admin.ModelAdmin):
    list_display=["id","otp","coustmer"]

@admin.register(CreditCardDetails)
class adminCreditCardDetails(admin.ModelAdmin):
    list_display=["id","credit_card_no","cvv","ex_date","created_at","coustmer1"]