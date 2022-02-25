import imp
from django.contrib import admin
from .models import addimg
# Register your models here.
@admin.register(addimg)
class addimg(admin.ModelAdmin):
    list_display=['im']