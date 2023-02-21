# Generated by Django 4.1 on 2023-01-23 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coustmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile')),
                ('first_name', models.CharField(max_length=90)),
                ('last_name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=90, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('pin', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=150)),
                ('pan_card', models.CharField(max_length=12, unique=True)),
                ('pan_photo', models.ImageField(upload_to='adharacard')),
                ('addhar_card', models.CharField(max_length=12, unique=True)),
                ('adhar_f', models.ImageField(upload_to='adharacard')),
                ('adhar_b', models.ImageField(upload_to='adharacard')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stafuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_no', models.IntegerField(unique=True)),
                ('cvv', models.IntegerField()),
                ('ex_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('coustmer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staf.coustmer')),
            ],
        ),
        migrations.CreateModel(
            name='CoustmerOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=4)),
                ('coustmer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staf.coustmer')),
            ],
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(default='16711040000', max_length=16, unique=True)),
                ('coustmerid', models.CharField(default='8658', max_length=8, unique=True)),
                ('balance', models.FloatField(default=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('types', models.CharField(default='saving', max_length=12)),
                ('Branch', models.CharField(default='kakatpur', max_length=30)),
                ('ModeofOperation', models.CharField(default='Single', max_length=30)),
                ('ifsc_code', models.CharField(default='fi0001671', max_length=12)),
                ('status', models.BooleanField(default=False)),
                ('mpin', models.CharField(max_length=4)),
                ('coustmer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staf.coustmer')),
            ],
        ),
    ]