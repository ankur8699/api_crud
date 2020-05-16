from rest_framework import routers
from second.viewsets import ProductsViewset

router=routers.DefaultRouter()
router.register('Products',ProductsViewset)