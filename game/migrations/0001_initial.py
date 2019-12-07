# Generated by Django 2.1.7 on 2019-05-17 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, help_text='Informações relevantes', null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Digite seu nome')),
                ('idade', models.IntegerField(max_length=3)),
                ('celular', models.IntegerField(max_length=13, verbose_name='Digie o seu numeor de telefone celular')),
                ('nascimento', models.DateField(verbose_name='Sua data de Nascimento')),
                ('email', models.EmailField(max_length=100)),
                ('Cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Cidade')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Estado'),
        ),
    ]
