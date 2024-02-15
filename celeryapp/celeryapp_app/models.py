from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    """Model class for authors"""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    """Model class for books"""

    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)
    
    def __unicode__(self):
        return self.title

class Review(models.Model):
    """Model class for user reviews of books"""

    user = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    book = models.ForeignKey(Book,on_delete = models.DO_NOTHING)
    timestamp = models.DateTimeField()
    rent = models.DateField()
    #what the user had to say about the book
    review_message = models.TextField()
    #ratings go from 1-5
    rating = models.IntegerField(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
    )

    def __unicode__(self):
        return self.user.username + " : " + self.book.title