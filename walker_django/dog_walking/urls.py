from dynamic_rest import routers
from . import viewsets

router = routers.DynamicRouter()

router.register_resource(viewsets.PersonViewSet)
router.register_resource(viewsets.DogViewSet)

urlpatterns = router.urls
