from django.contrib import admin
from .models import Info, Portfolio, PortfolioScreenshots, PortfolioDoneThings, Reviews, Services, Like

admin.site.register(Info)
admin.site.register(Portfolio)
admin.site.register(PortfolioScreenshots)
admin.site.register(PortfolioDoneThings)
admin.site.register(Reviews)
admin.site.register(Services)

