from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('properties', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, db_index=True)),
                ('sub_location_name', models.CharField(max_length=100, db_index=True)),
            ],
            options={
                'unique_together': {('city_name', 'sub_location_name')},
            },
        ),
    ]