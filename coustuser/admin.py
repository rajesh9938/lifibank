from django.contrib import admin
from .models import Transactions
# Register your models here.
@admin.register(Transactions)
class adminuser(admin.ModelAdmin):
    list_display = ["transaction_no","account","created_at","amount","withdraw_no","status"]