# Generated by Django 4.2.5 on 2024-04-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('DEVICEID', models.CharField(max_length=255)),
                ('NAME', models.CharField(blank=True, max_length=255, null=True)),
                ('WORKGROUP', models.CharField(blank=True, max_length=255, null=True)),
                ('USERDOMAIN', models.CharField(blank=True, max_length=255, null=True)),
                ('OSNAME', models.CharField(blank=True, max_length=255, null=True)),
                ('OSVERSION', models.CharField(blank=True, max_length=255, null=True)),
                ('OSCOMMENTS', models.CharField(blank=True, max_length=255, null=True)),
                ('PROCESSORT', models.CharField(blank=True, max_length=255, null=True)),
                ('PROCESSORS', models.IntegerField(default=0)),
                ('PROCESSORN', models.SmallIntegerField(blank=True, null=True)),
                ('MEMORY', models.IntegerField(blank=True, null=True)),
                ('SWAP', models.IntegerField(blank=True, null=True)),
                ('IPADDR', models.CharField(blank=True, max_length=255, null=True)),
                ('DNS', models.CharField(blank=True, max_length=255, null=True)),
                ('DEFAULTGATEWAY', models.CharField(blank=True, max_length=255, null=True)),
                ('ETIME', models.DateTimeField(blank=True, null=True)),
                ('LASTDATE', models.DateTimeField(blank=True, null=True)),
                ('LASTCOME', models.DateTimeField(blank=True, null=True)),
                ('QUALITY', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('FIDELITY', models.BigIntegerField(default=1)),
                ('USERID', models.CharField(blank=True, max_length=255, null=True)),
                ('TYPE', models.IntegerField(blank=True, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=255, null=True)),
                ('WINCOMPANY', models.CharField(blank=True, max_length=255, null=True)),
                ('WINOWNER', models.CharField(blank=True, max_length=255, null=True)),
                ('WINPRODID', models.CharField(blank=True, max_length=255, null=True)),
                ('WINPRODKEY', models.CharField(blank=True, max_length=255, null=True)),
                ('USERAGENT', models.CharField(blank=True, max_length=50, null=True)),
                ('CHECKSUM', models.BigIntegerField(default=262143)),
                ('SSTATE', models.IntegerField(default=0)),
                ('IPSRC', models.CharField(blank=True, max_length=255, null=True)),
                ('UUID', models.CharField(blank=True, max_length=255, null=True)),
                ('ARCH', models.CharField(blank=True, max_length=10, null=True)),
                ('CATEGORY_ID', models.IntegerField(blank=True, null=True)),
                ('ARCHIVE', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hardware',
                'managed': False,
            },
        ),
    ]
