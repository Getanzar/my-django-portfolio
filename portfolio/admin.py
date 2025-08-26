from django.contrib import admin
from .models import Project
from .models import Profile, Review
from .models import ContactMessage

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(ContactMessage)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    search_fields = ('author', 'text')

# Register your models here.
