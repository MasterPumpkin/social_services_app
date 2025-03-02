from django.contrib import admin
from .models import Client
from django.utils.html import format_html
from django import forms
import qrcode  # Import qrcode here
from io import BytesIO
from django.core.files.base import ContentFile

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Always generate qr_code, even if it was previously None:
        instance.generate_qr_code()  # No longer check if qr_code is empty
        if commit:
            instance.save()
        return instance


class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    list_display = ('first_name', 'last_name', 'address', 'phone', 'show_qr_code')
    readonly_fields = ('show_qr_code',)

    def show_qr_code(self, obj):
        if obj.qr_code:
            return format_html(f'<img src="{obj.qr_code.url}" width="150" height="150" />') # Changed
        return "No QR Code"
    show_qr_code.short_description = "QR Code"

admin.site.register(Client, ClientAdmin)