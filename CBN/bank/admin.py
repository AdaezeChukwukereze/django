from django.contrib import admin
from .models import Bank
from .models import Customer

admin.site.register(Bank)
admin.site.register(Customer)
