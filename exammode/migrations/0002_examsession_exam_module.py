# Generated by Django 2.2.3 on 2019-08-05 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0044_auto_20190415_1807'),
        ('exammode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsession',
            name='exam_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseModule'),
        ),
    ]
