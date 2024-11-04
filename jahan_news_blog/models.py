from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profilemedia/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profile"
    
    class Meta:
        verbose_name = "User Profile"      
        verbose_name_plural = "User Profiles"

class NewsArticleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    related_media = models.ImageField(upload_to='newsmedia/', blank=True, null=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    date_written = models.DateField(auto_now_add=True)

    def __str__(self):
        truncated_title = ' '.join(self.title.split()[:30])  
        return f"{truncated_title}, Author: {self.author.username if self.author else 'Unknown'}"
    
    class Meta:
        verbose_name = "News Article"      
        verbose_name_plural = "News Articles"

class NewsCommentsModel(models.Model):
    commentor = models.ForeignKey(UserProfileModel, on_delete=models.SET_NULL, null=True, blank=True)
    news = models.ForeignKey(NewsArticleModel, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField(max_length=200)
    approved = models.BooleanField(default=True)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        truncated_title = ' '.join(self.body.split()[:30])  
        return f"{truncated_title}, Commentor: {self.commentor.user.username if self.commentor else 'Unknown'}"
    
    class Meta:
        verbose_name = "News Comment"      
        verbose_name_plural = "News Comments"