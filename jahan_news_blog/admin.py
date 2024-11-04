from django.contrib import admin
from .models import UserProfileModel,NewsArticleModel,NewsCommentsModel
# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(NewsArticleModel)
admin.site.register(NewsCommentsModel)

