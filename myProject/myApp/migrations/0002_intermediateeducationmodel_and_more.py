# Generated by Django 5.1 on 2024-09-22 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntermediateEducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education_Name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntermediateExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experience_Name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntermediateInterestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interest_Name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntermediateLanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language_Name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntermediateSkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('My_Skill_Name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_No', models.CharField(max_length=100, null=True)),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('Profile_Pic', models.ImageField(null=True, upload_to='Media/Profile_Pic')),
                ('Carrer_Summary', models.CharField(max_length=100, null=True)),
                ('Age', models.PositiveIntegerField(null=True)),
                ('Gender', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education_Name', models.CharField(max_length=100, null=True)),
                ('Education_Choices', models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('honurs', 'Honurs')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Education_Name')},
            },
        ),
        migrations.CreateModel(
            name='ExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experience_Name', models.CharField(max_length=100, null=True)),
                ('Experience_Choices', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Experience_Name')},
            },
        ),
        migrations.CreateModel(
            name='InterestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interest_Name', models.CharField(max_length=100, null=True)),
                ('Interest_Choices', models.CharField(choices=[('sports', 'Sports'), ('music', 'Music'), ('reading', 'Reading')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Interest_Name')},
            },
        ),
        migrations.CreateModel(
            name='LanguageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language_Name', models.CharField(max_length=100, null=True)),
                ('Proficiency_Level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Language_Name')},
            },
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_Name', models.CharField(max_length=100, null=True)),
                ('Skill_Level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('expert', 'Expert')], max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'Skill_Name')},
            },
        ),
    ]