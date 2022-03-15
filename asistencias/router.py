from rest_framework import routers
from apps.persona import api


# Initializar el router de DRF solo una vez
router = routers.DefaultRouter()

# Registrar los ViewSet
router.register('persona', api.PersonaViewSet)
