# Generated by Django 4.1.7 on 2023-03-16 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(max_length=2000, verbose_name='полное_описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='время_создания')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='время_обновления')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='webapp.project', verbose_name='проект'),
        ),
    ]
