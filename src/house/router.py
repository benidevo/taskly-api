from rest_framework import routers

from house.viewsets import HouseViewSet

app_name = 'house'

router = routers.DefaultRouter()
router.register('houses', HouseViewSet)
