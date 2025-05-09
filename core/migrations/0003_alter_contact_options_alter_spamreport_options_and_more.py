# Generated by Django 5.2 on 2025-04-06 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contact', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='spamreport',
            options={'verbose_name': 'spam report', 'verbose_name_plural': 'spam reports'},
        ),
        migrations.RemoveField(
            model_name='spamreport',
            name='report_count',
        ),
        migrations.RemoveField(
            model_name='spamreport',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AddField(
            model_name='user',
            name='spam_reported',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='spamreport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='spamreport',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='spamreport',
            name='reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spam_reports', to=settings.AUTH_USER_MODEL, verbose_name='reporter'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(help_text='Required. 15 characters or fewer. Digits only.', max_length=15, unique=True, verbose_name='phone number'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['phone_number'], name='core_contac_phone_n_02cc9a_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['name'], name='core_contac_name_8f709f_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['owner', 'phone_number'], name='core_contac_owner_i_17ddae_idx'),
        ),
        migrations.AddIndex(
            model_name='spamreport',
            index=models.Index(fields=['phone_number'], name='core_spamre_phone_n_884930_idx'),
        ),
        migrations.AddIndex(
            model_name='spamreport',
            index=models.Index(fields=['reporter', 'phone_number'], name='core_spamre_reporte_9c3926_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['phone_number'], name='core_user_phone_n_59ea9a_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['first_name', 'last_name'], name='core_user_first_n_7ed624_idx'),
        ),
    ]
