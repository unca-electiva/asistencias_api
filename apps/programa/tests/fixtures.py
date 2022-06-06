import pytest

from apps.programa.models import TipoAsistencia, Programa


def crear_tipo_asistencia(descripcion, tipo):
    tipo_asistencia, _ = TipoAsistencia.objects.get_or_create(
        descripcion=descripcion,
        tipo=tipo
    )
    return tipo_asistencia


def crear_programa(nombre, fecha_inicio, fecha_fin, requisitos, *tipo_asistencias):
    programa, _ = Programa.objects.get_or_create(
        nombre=nombre,
        fecha_inicio=fecha_inicio,
        defaults={
            'requisitos': requisitos,
            'fecha_fin': fecha_fin
        }
    )

    if tipo_asistencias:
        for tipo in tipo_asistencias:
            programa.tipo_asistencias.add(tipo)

    return programa


@pytest.fixture
def crear_programas():
    programa1 = crear_programa('COVID', '2022-05-06', None, None,
                               crear_tipo_asistencia('Ayuda monetaria', 'dinero'),
                               crear_tipo_asistencia('Ayuda de materiales', 'material_construccion'),
                               crear_tipo_asistencia('Ayuda alimentaria', 'comida'))

    programa2 = crear_programa('ASISTENCIA ALIMENTICIA', '2022-05-06', None, None,
                               crear_tipo_asistencia('Ayuda alimentaria', 'comida'),
                               )

    return programa1, programa2
