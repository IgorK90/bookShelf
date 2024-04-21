from django.db import models


class Author(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return f"name:{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author,on_delete= models.CASCADE, null = False)

    def __str__(self):
        return f"name:{self.name} author:{self.author}"

class Shop(models.Model):
    name = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.name}"