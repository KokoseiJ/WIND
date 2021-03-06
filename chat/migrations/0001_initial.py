# Generated by Django 3.1.2 on 2020-11-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=10, verbose_name='name')),
                ('UserId', models.EmailField(max_length=50, verbose_name='id')),
                ('UserPassword', models.CharField(max_length=24, verbose_name='password')),
                ('UserDepartment', models.CharField(choices=[('information', '정보보호과'), ('software', '소프트웨어과'), ('business', 'IT경영학과'), ('design', '콘텐츠디자인과')], max_length=11, verbose_name='department')),
                ('UserStudentId', models.PositiveSmallIntegerField(verbose_name='student_id')),
                ('UserProfile', models.ImageField(blank=True, height_field=64, null=True, upload_to='', verbose_name='profile_image', width_field=64)),
                ('UserStatus', models.BooleanField(verbose_name='status')),
                ('UserFavorite', models.CharField(blank=True, max_length=2048, null=True, verbose_name='favorite')),
            ],
            options={
                'ordering': ['UserId'],
            },
        ),
    ]
