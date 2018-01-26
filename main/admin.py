from django.contrib import admin
from .models import *
from django import forms

# Register your models here.
admin.site.register(Client)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(Configuration)


class OrderAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Order
        fields = '__all__'

class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('orderStatus', 'noOfWorkers', 'orderDate')
    list_filter = ('orderStatus',)


admin.site.register(Order, OrderAdmin)
