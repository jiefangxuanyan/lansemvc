from django.db import models


class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Name


class Book(models.Model):
    ISBN = models.BigIntegerField(primary_key=True)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.DateField()
    Price = models.DecimalField(max_digits=100, decimal_places=2)

    def __unicode__(self):
        return self.Title
