<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
"""
URL configuration for atbapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
from django.urls import include, path
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from django.conf import settings
<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
=======

urlpatterns = [
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include('users.urls')),
]

<<<<<<< HEAD
urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
=======
urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
=======
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
from django.contrib import admin
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/users/', include('users.urls')),
]
=======
<<<<<<< HEAD

    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]
=======
    path('api/', include('users.urls')),
]
>>>>>>> 5f3157850eb87e28d70d2e6f1d58428d66ca0ed6
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
>>>>>>> 03e93217a6fbd32a2ead0a15f9d43ce459b8c8e7
