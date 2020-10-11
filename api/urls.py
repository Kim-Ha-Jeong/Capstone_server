from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'full', FullViewSet)
router.register(r'edited', EditedViewSet)

urlpatterns = router.urls