# Generated by Django 4.1.5 on 2023-01-11 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=168, verbose_name='Название объекта')),
                ('square', models.IntegerField(default=0, verbose_name='Площадь объекта, м2')),
                ('preview', models.TextField(max_length=250, verbose_name='Предпросмотр')),
                ('text', models.TextField(verbose_name='Текст по объекту')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Актуальность объекта')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('object_status', models.BooleanField(db_index=True, default=True, verbose_name='Завершен ли объект')),
                ('main_photo', models.ImageField(blank=True, null=True, upload_to='object_photos/', verbose_name='Главное фото')),
                ('video', models.TextField(blank=True, max_length=40, verbose_name='Cсылка на видео')),
                ('function_light', models.BooleanField(default=True, verbose_name='Функционал: Освещение')),
                ('function_shutters', models.BooleanField(default=False, verbose_name='Функционал: Шторы')),
                ('function_ventilation', models.BooleanField(default=False, verbose_name='Функционал: Вентиляция')),
                ('function_condition', models.BooleanField(default=False, verbose_name='Функционал: Кондиционирование')),
                ('function_warm_floors', models.BooleanField(default=False, verbose_name='Функционал: Теплые полы')),
                ('function_security', models.BooleanField(default=False, verbose_name='Функционал: Безопасность')),
                ('function_remote', models.BooleanField(default=False, verbose_name='Функционал: Удаленное управление')),
                ('function_voice_control', models.BooleanField(default=False, verbose_name='Функционал: Голосовые помощники')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='object_photos/')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Актуальность фото')),
                ('object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object', to='portfolioapp.portfolioobject', verbose_name='Объект')),
            ],
        ),
    ]
