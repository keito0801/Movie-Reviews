from django.contrib import admin
from .models import Movie, Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):

    model = Review
    list_display = ('user_name', 'comment', 'rating')
    list_filter = ['user_name']
    search_fields = ['comment']

#admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)