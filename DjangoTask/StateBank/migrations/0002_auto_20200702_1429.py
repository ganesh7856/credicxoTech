# Generated by Django 3.0.8 on 2020-07-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StateBank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch_name',
            name='bank',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Bank_Name',
        ),
    ]