# Generated by Django 4.0.6 on 2022-07-09 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_participant_meetup_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('OrgEmail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2022-01-26'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='Organizer',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.organizer'),
        ),
    ]