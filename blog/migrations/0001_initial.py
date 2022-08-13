# Generated by Django 3.2.13 on 2022-07-14 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Title')),
                ('title_en', models.CharField(db_index=True, max_length=50, null=True, verbose_name='Title')),
                ('title_az', models.CharField(db_index=True, max_length=50, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=70)),
                ('slug_en', models.SlugField(blank=True, editable=False, max_length=70, null=True)),
                ('slug_az', models.SlugField(blank=True, editable=False, max_length=70, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_az', models.TextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='product.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='blog_tags', to='core.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('subject', models.CharField(db_index=True, max_length=80, verbose_name='subject')),
                ('review', models.TextField(verbose_name='Comments')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogcomment', to='blog.blog')),
                ('reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]