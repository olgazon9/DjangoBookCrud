from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Loaner, Loan
from .serializers import BookSerializer, LoanerSerializer, LoanSerializer

# API endpoint for listing all books or creating a new book
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API endpoint for retrieving, updating, or deleting a specific book
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API endpoint for listing all loaners or creating a new loaner
@api_view(['GET', 'POST'])
def loaner_list(request):
    if request.method == 'GET':
        loaners = Loaner.objects.all()
        serializer = LoanerSerializer(loaners, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API endpoint for retrieving, updating, or deleting a specific loaner
@api_view(['GET', 'PUT', 'DELETE'])
def loaner_detail(request, pk):
    try:
        loaner = Loaner.objects.get(pk=pk)
    except Loaner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanerSerializer(loaner)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanerSerializer(loaner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loaner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API endpoint for listing all loans or creating a new loan
@api_view(['GET', 'POST'])
def loan_list(request):
    if request.method == 'GET':
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
