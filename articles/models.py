from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # this is an automatic URL that shows one object
        return reverse('article_detail', args=[str(self.id)])
#related name describes reverse relation between article and comments  .. * comments ---> 1 article = FK relation
class Comment(models.Model):  #get_user_model is used to reference our custom user
    article = models.ForeignKey(Article, on_delete=models.CASCADE , related_name='comments')  #FOO_set t3ayet lil comments (FK relation) we want to change Foo_set so we use related_name
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):   #we always add str and get absolute url
        return  self.comment

    def  get_absolute_url(self):  #redirection url after an operation
        return reverse('article_list')
