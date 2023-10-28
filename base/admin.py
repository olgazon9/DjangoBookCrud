from django.contrib import admin
from .models import Book,Loan,Loaner

admin.site.register(Book)
admin.site.register(Loaner)
admin.site.register(Loan)
# Register your models here.
