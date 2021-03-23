from django.contrib import admin
from . import models

# ordering fileds

class MovieAdmin(admin.ModelAdmin):

    fields=['release_year','title','length']

    # to ad search
    search_fields=['title','length']

    # to create filter
    list_filter=['release_year','length']

    # to add fields
    list_display= ['title','release_year','length']

    # editable listview
    list_editable=['length']






# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
