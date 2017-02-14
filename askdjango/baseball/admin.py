from django.contrib import admin
from .models import Stadium, Block, Seat


admin.site.register(Stadium)
admin.site.register(Block)

class SeatAdmin(admin.ModelAdmin):
    list_display = ['block', 'row', 'col', 'is_blind', 'photo']
    list_filter = ['block', 'is_blind']

admin.site.register(Seat, SeatAdmin)

