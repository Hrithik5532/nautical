from django.contrib import admin
from .models import * 
# Register your models here.

class profileDetailsAdmin(admin.ModelAdmin):
        
        list_display=('id',"fname","lname","email","nationality")

admin.site.register(profileDetails,profileDetailsAdmin)
admin.site.register(NKD)
admin.site.register(PassportDetails)
admin.site.register(CDCSB)
admin.site.register(AcademicDetails)
admin.site.register(LCOC)
admin.site.register(STCWCertificates)
admin.site.register(Reference)
admin.site.register(AboutUS)
admin.site.register(LDW)
admin.site.register(PersonalDetails)
admin.site.register(Additional_info)
admin.site.register(Reason_for_app)
admin.site.register(SEA_Exp)
admin.site.register(OSS)
admin.site.register(Declaration)
admin.site.register(NKD_de)
admin.site.register(ATOC)


