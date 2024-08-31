from django.contrib import admin
from .models import Department, Designation, Permission, Role, User

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)