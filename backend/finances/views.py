from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Category, Expense, Income
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing categories.
    Categories are visible to all authenticated users.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'type']


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing personal expenses.
    Users can only see and edit their own expenses.
    """
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'notes', 'category__name']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class IncomeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing personal income.
    Users can only see and edit their own income.
    """
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['description', 'notes', 'category__name']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)
