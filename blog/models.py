from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
STATUS = (
    ( 0, 'Draft'),
    (1, 'Publish')
)
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    exercise_title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.exercise_title
    def get_absolute_url(self):
        return reverse('blog_detail.html', kwargs=({'slug': self.slug}))

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80,default="Enter Name")
    email = models.EmailField(default= "enter email")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"