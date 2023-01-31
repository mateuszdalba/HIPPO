from django.contrib import admin

from .models import Disease, Medicine, Fasting


admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(Fasting)
