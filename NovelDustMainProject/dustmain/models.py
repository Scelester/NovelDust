from django.db import models

# Create your models here.
class TopBooks(models.Model):
    topname = models.CharField(max_length=200)
    topcover = models.ImageField(upload_to=None,blank=True,null=True)

    def __str__(self):
        return self.topname

class BookItems(models.Model):
    topbook = models.ForeignKey(TopBooks, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=None,blank=True,null=True)
    samename = models.BooleanField()
    samecover = models.BooleanField()
    volume_no = models.IntegerField()

    def __str__(self):
        return self.name



class Genrelist(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    topbook = models.ForeignKey(TopBooks, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genrelist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.genre)+ ' ['+ str(self.topbook)+']'