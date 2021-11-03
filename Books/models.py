from django.db import models

class Books(models.Model):
    """ Basic model to add a book in our db,
    requires a title, description, author and isbn """

    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.title
