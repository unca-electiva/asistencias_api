# Generated by Django 3.1 on 2022-05-04 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_delete_prueba'),
        ('programa', '0003_tipoasistencia_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacionbeneficio',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones_beneficios', to='persona.persona'),
        ),
        migrations.AlterField(
            model_name='asignacionbeneficio',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones_beneficios', to='programa.programa'),
        ),
    ]
