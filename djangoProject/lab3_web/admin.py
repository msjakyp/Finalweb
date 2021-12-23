from django.contrib import admin
from .models import Articles
from .models import Customers
from .models import Orders
# Register your models here.
admin.site.register(Articles)
admin.site.register(Customers)
admin.site.register(Orders)