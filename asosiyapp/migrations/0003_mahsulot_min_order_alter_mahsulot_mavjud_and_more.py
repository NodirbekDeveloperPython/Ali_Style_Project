# Generated by Django 4.1 on 2022-10-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0002_mahsulot_alter_ichki_bolim_rasm_mahsulot_ichki'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='min_order',
            field=models.CharField(default='1 dona', max_length=30),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='mavjud',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='nom',
            field=models.CharField(max_length=70),
        ),
    ]
