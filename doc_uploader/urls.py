from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'answer', AnswerViewSet, basename='answer')

urlpatterns = [
    path('', include(router.urls)),
]
