from django import forms
from django.contrib.auth.models import User
from .models import Order
from django.contrib.admin import widgets

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    mobile_number = forms.RegexField(regex=r'\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*', required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'mobile_number', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class OrderForm(forms.ModelForm):
    # orderDate = forms.DateField(widget=forms.TextInput(attrs=
    # {
    #     'class': 'datepicker'
    # }))
    # fromTime = forms.TimeField(widget=forms.TimeInput)

    class Meta:
        model = Order
        fields = ['orderType', 'vehicle', 'noOfWorkers', 'noOFHours', 'orderDate', 'fromTime', 'toTime']

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['orderDate'].widget = widgets.AdminDateWidget()
            self.fields['fromTime'].widget = widgets.AdminTimeWidget()
            self.fields['toTime'].widget = widgets.AdminTimeWidget()
