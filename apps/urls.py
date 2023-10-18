from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


from .views import LoginView, SponsorModelViewSet, StudentModelViewSet,SponsorModelUpdateViewSet

router = DefaultRouter()
router.register('users', LoginView, basename="users")
router1 = DefaultRouter()
router1.register('sponser', SponsorModelViewSet, basename='sponser')
router2 = DefaultRouter()
router2.register('student', StudentModelViewSet, basename='student')
router3 = DefaultRouter()
router3.register('sponser-update', SponsorModelUpdateViewSet, basename='sponser-update')
urlpatterns = [
    path('users/', include(router.urls)),
    path('sponser/', include(router1.urls)),
    path('sponser-update/', include(router3.urls)),
    path('student/', include(router2.urls)),
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
