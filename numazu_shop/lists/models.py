from django.db import models


# 店
class Shop(models.Model):
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=512, null=True)
    desc = models.TextField(max_length=512, null=True)

    def __str__(self):
        return f"{self.title} {self.link} {self.desc}"


# 記事
class Article(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=512, null=True)
    text = models.TextField(max_length=512)
    src_url = models.CharField(max_length=512, null=True)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return f"{self.text}" 
