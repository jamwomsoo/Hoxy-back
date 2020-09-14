from django.contrib import admin
from waste.models import waste_div
from waste.models import waste_type
from waste.models import board
from waste.models import board_review
from waste.models import area
from waste.models import apply_info
from waste.models import user_info
from waste.models import forpay
# Register your models here.
admin.site.register(waste_div)
admin.site.register(waste_type)
admin.site.register(board)
admin.site.register(board_review)
admin.site.register(area)
admin.site.register(apply_info)
admin.site.register(user_info)
admin.site.register(forpay)