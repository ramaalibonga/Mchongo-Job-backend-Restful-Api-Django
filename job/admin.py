from django.contrib import admin
from .models import JobDetails,UserAccount,EmailList,Address,Location
# Register your models here.
admin.site.site_header = "Mchongo Job Admin"
admin.site.site_title = "Mchongo Job Admin Portal"
admin.site.index_title = "Welcome to Mchongo Job Portal"

admin.site.register(JobDetails)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(EmailList)
admin.site.register(UserAccount)

