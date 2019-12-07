# Generated by Django 2.2.2 on 2019-08-31 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=2)),
                ('senha', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Digite seu nome')),
                ('marca', models.CharField(max_length=50, verbose_name='Digite a marca')),
                ('descricao', models.CharField(max_length=50, verbose_name='Digite a descrição da plataforma')),
            ],
        ),
        migrations.AlterField(
            model_name='estado',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='celular',
            field=models.IntegerField(max_length=13, verbose_name='Digie o seu numero de telefone celular'),
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Digite o nome do jogo')),
                ('descricao', models.CharField(max_length=50, verbose_name='Digite uma breve descrição')),
                ('Plataforma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Plataforma')),
            ],
        ),
    ]
