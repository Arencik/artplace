# Generated by Django 4.1.7 on 2023-05-09 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_options'),
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conversation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='item.item'),
        ),
    ]
