from rest_framework import routers
from .views import PortfolioViewSet

router = routers.SimpleRouter()
router.register(r'api', PortfolioViewSet)
urlpatterns = router.urls