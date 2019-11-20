from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Document)
admin.site.register(Customer)
admin.site.register(Profession)
admin.site.register(DataSheet)
