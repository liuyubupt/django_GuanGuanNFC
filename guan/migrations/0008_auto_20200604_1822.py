# Generated by Django 3.0.3 on 2020-06-04 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guan', '0007_auto_20200604_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='activity',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='actsta',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='actsta',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='application',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='application',
            name='from_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guan.UserInfo'),
        ),
        migrations.AlterField(
            model_name='application',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='box',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='box',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='boxcontent',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='boxcontent',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='friend',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='friend',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='pushnote',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='pushnote',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='created_time',
            field=models.BigIntegerField(default=1591294971),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='updated_time',
            field=models.BigIntegerField(default=1591294971),
        ),
    ]