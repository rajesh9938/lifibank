# Generated by Django 4.1 on 2023-02-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staf', '0005_alter_creditcarddetails_ex_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcarddetails',
            name='ex_date',
            field=models.DateTimeField(),
        ),
    ]
