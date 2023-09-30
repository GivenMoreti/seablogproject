from django.contrib import admin
from .models import Current,Topic,Post
from django.contrib.auth.models import User, Group
# Register your models here.
class CurrentModel(admin.ModelAdmin):
    list_display = ('name','description')

class PostModel(admin.ModelAdmin):
    list_display = ('message','topic','created_at','updated_at','created_by','updated_by')

class TopicModel(admin.ModelAdmin):
    list_display = ('subject','current','starter','last_updated')

admin.site.register(Current,CurrentModel)
admin.site.register(Post,PostModel)
admin.site.register(Topic,TopicModel)





