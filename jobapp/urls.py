
from django.contrib import admin
from django.urls import path,include
from job.views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('',include('job.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
