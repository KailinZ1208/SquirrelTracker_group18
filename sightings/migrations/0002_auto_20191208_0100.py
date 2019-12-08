# Generated by Django 3.0 on 2019-12-08 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sight',
            name='Runs_from',
        ),
        migrations.RemoveField(
            model_name='sight',
            name='Tail_flags',
        ),
        migrations.RemoveField(
            model_name='sight',
            name='Tail_twitches',
        ),
        migrations.AddField(
            model_name='sight',
            name='Runs_From',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Runs_From', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='sight',
            name='Tail_Flags',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Tail_Flags', max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='sight',
            name='Tail_Twitches',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Tail_Twiches', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), (None, '-'), ('?', '?')], help_text='Age of the squirrel', max_length=16),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Approaches',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Approaches', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Chasing',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Chasing', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Climbing',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Climbing', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Date',
            field=models.IntegerField(help_text='Date of the sighting', null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Eating',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Eating', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Foraging',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Foraging', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Indifferent',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Indifferent', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Kuks',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Kuks', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Moans',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Moans', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Other_Activities',
            field=models.CharField(help_text='Other Activities', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Quaas',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Quaas', max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Running',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], default='FALSE', help_text='Running', max_length=16, null=True),
        ),
    ]
