from django.db import models
from django.contrib.auth.models import User



# list of genre to append to topbook
class Genrelist(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# for bookname and cover that will actually show upfront.
class TopBooks(models.Model):
    topname = models.CharField(max_length=200)
    topcover = models.ImageField(null=True,blank=True,upload_to='media/topcovers/%Y-%m')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genrelist)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.topname

    def title_to_url(self):
        return self.topname.replace(' ','-')


# for bookitems to put inside the topcover
class BookItems(models.Model):
    topbook = models.ForeignKey(TopBooks, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000,null=True)
    volume_no = models.IntegerField()
    
    def file_name_path(self, filename):
        return f'media/bookfiles/{self.topbook.topname}/{filename}'

    bookfile = models.URLField(max_length=1000,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






class BookRequests(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topbook = models.ForeignKey(TopBooks,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class BookLikes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topbook = models.ForeignKey(TopBooks,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

