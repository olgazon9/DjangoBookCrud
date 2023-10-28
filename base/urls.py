from django.urls import path
from .views import book_list, book_detail, loaner_list, loaner_detail, loan_list

urlpatterns = [
    # Book URLs
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),

    # Loaner URLs
    path('loaners/', loaner_list, name='loaner-list'),
    path('loaners/<int:pk>/', loaner_detail, name='loaner-detail'),

    # Loan URLs
    path('loans/', loan_list, name='loan-list'),
]
