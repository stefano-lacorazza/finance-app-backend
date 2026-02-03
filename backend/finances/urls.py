from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ExpenseViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'incomes', IncomeViewSet, basename='income')

urlpatterns = [
    path('', include(router.urls)),
]
