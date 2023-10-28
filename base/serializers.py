# serializers.py
from rest_framework import serializers
from .models import Book, Loaner, Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LoanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loaner
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
