# Generated by Django 4.1 on 2023-01-27 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staf', '0001_initial'),
        ('coustuser', '0003_alter_transactions_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staf.accountdetails'),
        ),
    ]