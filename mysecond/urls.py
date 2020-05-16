from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from second.views import ProductListView , ProductDetailView  , PostListView
from .router import router

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('view/products/', ProductListView.as_view(), name='product-list'),
    path('view/products/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('list-create/', PostListView.as_view(), name='list-create'),
    path('api/',include(router.urls)),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)