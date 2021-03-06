# Generated by Django 4.0.3 on 2022-06-28 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_note_post_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='post_time',
            new_name='note_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='note',
        ),
        migrations.AddField(
            model_name='note',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note_on_contact', to='contacts.contact'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
