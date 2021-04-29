from django.contrib import admin

# Register your models here.
from ski_resort.models import BoardRentModel, SkiRentModel, BootsRentModel, Choices

admin.site.register(BoardRentModel)
admin.site.register(SkiRentModel)
admin.site.register(BootsRentModel)
admin.site.register(Choices)
