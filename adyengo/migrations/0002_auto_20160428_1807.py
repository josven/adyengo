# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-28 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adyengo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='res_url',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='recurringpaymentresult',
            name='result_code',
            field=models.CharField(choices=[('Authorised', 'Authorised'), ('Error', 'Error'), ('Refused', 'Refused')], max_length=30),
        ),
        migrations.AlterField(
            model_name='session',
            name='country_code',
            field=models.CharField(blank=True, choices=[('DE', 'Germany'), ('NL', 'Netherlands'), ('GB', 'United Kingdom'), ('BE', 'Belgium')], max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_type',
            field=models.CharField(choices=[('hpp_regular', 'HPP Regular'), ('api_recurring', 'API Recurring'), ('hpp_recurring', 'HPP Recurring')], max_length=25),
        ),
        migrations.AlterField(
            model_name='session',
            name='shopper_locale',
            field=models.CharField(blank=True, choices=[('fr_BE', 'French (Belgium)'), ('nl_NL', 'Dutch (Holland)'), ('de_DE', 'German (Germany)'), ('en_GB', 'English (United Kingdom)'), ('nl_BE', 'Dutch (Belgium)')], default='nl_NL', max_length=5),
        ),
        migrations.AlterField(
            model_name='sessionallowedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('bankTransfer', 'All banktransfers'), ('ideal', 'iDEAL'), ('bankTransfer_DE', 'German Banktransfer'), ('card', 'All debit and credit cards'), ('visa', 'Visa'), ('elv', 'ELV'), ('directEbanking', 'SofortUberweisung'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('amex', 'Amex'), ('mc', 'Master Card'), ('paypal', 'PayPal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionblockedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('bankTransfer', 'All banktransfers'), ('ideal', 'iDEAL'), ('bankTransfer_DE', 'German Banktransfer'), ('card', 'All debit and credit cards'), ('visa', 'Visa'), ('elv', 'ELV'), ('directEbanking', 'SofortUberweisung'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('amex', 'Amex'), ('mc', 'Master Card'), ('paypal', 'PayPal')], max_length=50),
        ),
    ]
