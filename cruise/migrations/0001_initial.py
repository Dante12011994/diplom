# Generated by Django 4.2.7 on 2023-11-27 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название круиза')),
                ('data_start', models.DateField(verbose_name='Дата начала')),
                ('date_finish', models.DateField(verbose_name='Дата окончания')),
                ('town_start', models.CharField(max_length=150, verbose_name='Город начала')),
                ('town_finish', models.CharField(max_length=150, verbose_name='Город окончания')),
                ('status_cruise', models.CharField(choices=[('create', 'Рейс состоится'), ('start', 'Круиз начался'), ('finished', 'Круиз завершен')], default='create', max_length=8)),
                ('length', models.PositiveIntegerField(verbose_name='Продолжительность')),
            ],
            options={
                'verbose_name': 'Круиз',
                'verbose_name_plural': 'Круизы',
            },
        ),
        migrations.CreateModel(
            name='Ships',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название теплохода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото корабля')),
            ],
            options={
                'verbose_name': 'Теплоход',
                'verbose_name_plural': 'Теплоходы',
            },
        ),
        migrations.CreateModel(
            name='Prise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('standart', 'стандартная каюта'), ('deluxe', 'каюта де-люкс'), ('luxe', 'каюта люкс')], max_length=8, verbose_name='Класс каюты')),
                ('prise', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('cruise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruise.cruise', verbose_name='Круиз')),
            ],
            options={
                'verbose_name': 'Стоимость',
                'verbose_name_plural': 'Стоимости',
            },
        ),
        migrations.AddField(
            model_name='cruise',
            name='ship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruise.ships', verbose_name='Теплоход'),
        ),
    ]
