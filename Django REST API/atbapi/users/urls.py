<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
=======
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
]
>>>>>>> 5f3157850eb87e28d70d2e6f1d58428d66ca0ed6
