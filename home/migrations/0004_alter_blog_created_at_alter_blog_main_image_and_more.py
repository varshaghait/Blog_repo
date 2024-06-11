# Generated by Django 5.0.6 on 2024-05-30 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_blog_created_at_alter_blog_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(default='', upload_to='blogs'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
