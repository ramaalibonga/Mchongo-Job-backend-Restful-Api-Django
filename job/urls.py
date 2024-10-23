from django.urls import path,include
from .views import signin,signout,home,signup,create_email,details,description,search
from rest_framework import routers
from .views import EmailListViews,JobDetailsViews,AddressViews,LocationViews

router = routers.DefaultRouter()
router.register(r'email',EmailListViews)
router.register(r'jobdetails',JobDetailsViews)
router.register(r'address',AddressViews)
router.register(r'location',LocationViews)

#urlpatterns = [path('api/',include(router.urls),name="api")]

urlpatterns = [
    path('api/v1/',include(router.urls),name="api"),
    # path('login',signin,name="login-url"),
    # path('logout',signout,name="logout-url"),
    # path('email',create_email,name="email-url"),
    # path('signup',signup,name="signup-url"),
    # path('home',home,name="home-url"),
    # path('details',details,name="details"),
    # path('description/<id>',description,name="description"),
    # path('search',search,name="search")
]