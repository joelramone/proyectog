from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Ticketview
router = DefaultRouter()
router.register('data', GetMethod, basename='data')
urlpatterns = router.urls

urlpatterns = [
    path('ticket/', Ticketview.as_view(), name='datos'),
]