from django.contrib import admin
from .models import Blog, UserFormSubmission

# Register your models here.
admin.site.register(Blog)
admin.site.register(UserFormSubmission)