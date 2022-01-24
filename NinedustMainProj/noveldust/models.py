from django.db import models



# list of genre to append to topbook
class Genrelist(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


# for bookname and cover that will actually show upfront.
class TopBooks(models.Model):
    topname = models.CharField(max_length=200)
    topcover = models.ImageField(upload_to='media/topcover/%Y-%m-%d')
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genrelist)

    def __str__(self):
        return self.topname

    def title_to_url(self):
        return self.topname.replace(' ','-')


# for bookitems to put inside the topcover
class BookItems(models.Model):
    topbook = models.ForeignKey(TopBooks, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    cover = models.ImageField(upload_to=None,blank=True,null=True)
    samename = models.BooleanField()
    samecover = models.BooleanField()
    volume_no = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
