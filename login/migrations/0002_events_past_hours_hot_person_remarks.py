# Generated by Django 2.2.7 on 2019-12-18 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='past_hours_hot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('past_onehour_hot', models.IntegerField()),
                ('past_twohour_hot', models.IntegerField()),
                ('past_threehour_hot', models.IntegerField()),
                ('past_fourhour_hot', models.IntegerField()),
                ('past_fivehour_hot', models.IntegerField()),
                ('past_sixhour_hot', models.IntegerField()),
            ],
            options={
                'db_table': 'past_hours_hot',
            },
        ),
        migrations.CreateModel(
            name='person_remarks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('person1_name', models.CharField(max_length=255)),
                ('person1_remark', models.CharField(max_length=255)),
                ('person1_pic', models.CharField(max_length=255)),
                ('person2_name', models.CharField(max_length=255)),
                ('person2_remark', models.CharField(max_length=255)),
                ('person2_pic', models.CharField(max_length=255)),
                ('person3_name', models.CharField(max_length=255)),
                ('person3_reamrk', models.CharField(max_length=255)),
                ('person3_pic', models.CharField(max_length=255)),
                ('person4_name', models.CharField(max_length=255)),
                ('person4_reamrk', models.CharField(max_length=255)),
                ('person4_pic', models.CharField(max_length=255)),
                ('person5_name', models.CharField(max_length=255)),
                ('person5_reamrk', models.CharField(max_length=255)),
                ('person5_pic', models.CharField(max_length=255)),
                ('person6_name', models.CharField(max_length=255)),
                ('person6_reamrk', models.CharField(max_length=255)),
                ('person6_pic', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'person_remarks',
            },
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.CharField(max_length=255)),
                ('time', models.DateField()),
                ('neutral_remark', models.IntegerField()),
                ('passive_remark', models.IntegerField()),
                ('negative_remark', models.IntegerField()),
                ('famale', models.IntegerField()),
                ('male', models.IntegerField()),
                ('age_00', models.IntegerField()),
                ('age_90', models.IntegerField()),
                ('age_80', models.IntegerField()),
                ('age_70', models.IntegerField()),
                ('age_60', models.IntegerField()),
                ('past_hour_hot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.past_hours_hot')),
                ('relative_person_remark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.person_remarks')),
            ],
            options={
                'db_table': 'events',
                'ordering': ['-time'],
            },
        ),
    ]
