from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Advertisement,AddBanner,AddVideo,News,AddMashikPatrika,AajKaRashifal,CustomUser

from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.forms import Textarea


from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from ckeditor.widgets import CKEditorWidget




admin.site.register(CustomUser)
class NEWSAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(News,NEWSAdmin)


@admin.register(Advertisement)
class AdvertisemnetAdmin(admin.ModelAdmin):
    list_display = ('title',  'ctg','image','status')

@admin.register(AddBanner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image','status')

@admin.register(AddVideo)
class videoAdmin(admin.ModelAdmin):
    list_display = ('title','status','video')


@admin.register(AddMashikPatrika)
class AddMashikPatrikaAdmin(admin.ModelAdmin):
    list_display = ('title','image','pdf')

@admin.register(AajKaRashifal)
class AajKaRashifalAdmin(admin.ModelAdmin):
    pass
    #  list_display = ['description']


