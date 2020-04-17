# Generated by Django 3.0.4 on 2020-04-17 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200416_1828'),
    ]

    operations = [
        migrations.DeleteModel(
            name='projects',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='password',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.branch'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.college'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_role',
            field=models.ManyToManyField(null=True, through='user.user_roles', to='user.roles'),
        ),
    ]
