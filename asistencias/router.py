from rest_framework import routers
from apps.persona import api as api_persona
from apps.programa import api as api_programa


# Initializar el router de DRF solo una vez
router = routers.DefaultRouter()

# Registrar los ViewSet
router.register('persona', api_persona.PersonaViewSet)
router.register('estado-salud', api_persona.EstadoSaludViewSet)
router.register('programa', api_programa.ProgramaViewSet)
router.register('asignacion-beneficio', api_programa.AsignacionBeneficioViewSet)
