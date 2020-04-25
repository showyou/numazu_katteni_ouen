from django.db import models


# 店
class Shop(models.Model):
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=512, null=True)
    desc = models.TextField(max_length=512, null=True)

    def __str__(self):
        return f"{self.title}"


# 記事
class Article(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image_url1 = models.CharField(max_length=512, null=True)
    image_url2 = models.CharField(max_length=512, null=True)
    image_url3 = models.CharField(max_length=512, null=True)
    image_url4 = models.CharField(max_length=512, null=True)
    text = models.TextField(max_length=512)
    src_url = models.CharField(max_length=512, null=True)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return f"{self.text[0:20]}" 
