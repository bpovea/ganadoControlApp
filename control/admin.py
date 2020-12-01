from django.contrib import admin

from .models import *

admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(Livestock)
admin.site.register(Income)
admin.site.register(Outcome)
admin.site.register(LivestockWeightHistory)