from django.contrib import admin

from .models import CustomUser, Staff, Students, Gallery,Contact_us
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Staff)
admin.site.register(Students)
admin.site.register(Gallery)
admin.site.register(Contact_us)