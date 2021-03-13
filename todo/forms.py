from django import forms
form .models import Item


class ItemFrom(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']