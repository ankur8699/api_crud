from rest_framework import routers
from second.viewsets import ProductsViewset, DetailsViewset

router=routers.DefaultRouter()
router.register('Products',ProductsViewset)
router.register('Details',DetailsViewset)
