from rest_framework import serializers
from .models import Category, Expense, Income

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'description', 'created_at', 'updated_at']

class ExpenseSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = Expense
        fields = ['id', 'category', 'category_detail', 'amount', 'description', 'payment_method', 'notes', 'date', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class IncomeSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Income
        fields = ['id', 'category', 'category_detail', 'amount', 'description', 'notes', 'date', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
