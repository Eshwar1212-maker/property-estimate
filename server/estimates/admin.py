from django.contrib import admin

# Register your models here.
from .models import PropertyEstimate, PropertyInquiry

admin.site.register(PropertyEstimate)
admin.site.register(PropertyInquiry)
