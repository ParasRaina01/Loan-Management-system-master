# Generated by Django 3.2.3 on 2021-06-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_auto_20210601_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='interest_rate',
            field=models.DecimalField(decimal_places=3, max_digits=18),
        ),
        migrations.AlterField(
            model_name='loan',
            name='last_payment',
            field=models.DateTimeField(blank=True, null=True, verbose_name='recent payment'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_amount',
            field=models.DecimalField(decimal_places=3, max_digits=18),
        ),
        migrations.AlterField(
            model_name='loan',
            name='tenure',
            field=models.IntegerField(verbose_name='tenure in months'),
        ),
    ]
