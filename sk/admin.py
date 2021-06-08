from django.contrib import admin
from .models import SignUp,Library_vlink,Library_pdf,UserProfile,Profile,PrivateSetting
from .models import FileUpload
# Register your models here.
admin.site.register(SignUp)
admin.site.register(Library_pdf)
admin.site.register(Library_vlink)
admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(PrivateSetting)
admin.site.register(FileUpload)