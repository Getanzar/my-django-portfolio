from django.contrib import admin
from .models import Project
from .models import Profile, Review
from .models import ContactMessage

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(ContactMessage)

# Register your models here.
