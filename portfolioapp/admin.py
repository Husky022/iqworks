from django.contrib import admin


# Register your models here.
from .models import PortfolioObject, PortfolioImage

admin.site.register(PortfolioObject)
admin.site.register(PortfolioImage)
