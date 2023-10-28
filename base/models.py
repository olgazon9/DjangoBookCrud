from django.db import models

from django.db import models

# Model for a Book
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    year_published = models.PositiveIntegerField()
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    def __str__(self):
        return self.title

# Model for a Loaner
class Loaner(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

# Model for a Loan
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loaner = models.ForeignKey(Loaner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.loaner.name} - {self.book.title} Loan"

