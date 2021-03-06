# Generated by Django 2.2.5 on 2020-02-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200214_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_general', models.CharField(help_text='The general services desciption', max_length=8000)),
                ('services_webdesign', models.CharField(help_text='The webdesign services desciption', max_length=8000)),
                ('services_branding', models.CharField(help_text='The branding services desciption', max_length=8000)),
                ('services_photography', models.CharField(help_text='The photography services desciption', max_length=8000)),
                ('services_development', models.CharField(help_text='The development services desciption', max_length=8000)),
                ('services_ui', models.CharField(help_text='The ui services desciption', max_length=8000)),
                ('services_printing', models.CharField(help_text='The printing services desciption', max_length=8000)),
                ('portfolio_general', models.CharField(help_text='The portfolio general desciption', max_length=8000)),
            ],
        ),
    ]
