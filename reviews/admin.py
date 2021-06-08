from django.contrib import admin
from .models import Movie, Review


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):

    model = Review
    list_display = ('title','user_name', 'comment', 'rating')
    list_filter = ['title']
    search_fields = ['comment']

#admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)
