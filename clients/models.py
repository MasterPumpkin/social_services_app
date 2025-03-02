from django.db import models
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.text import slugify

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=50, default="Basic Visit")  # For MVP
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True) # Changed to ImageField
    notes = models.TextField(blank=True, null=True)
    contact_person_first_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_person_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(self.id))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a BytesIO object
        buffer = BytesIO()
        img.save(buffer, format='PNG')

        # Create a filename
        filename = f'qr_code-{slugify(self.first_name)}-{slugify(self.last_name)}-{self.id}.png'

        # Save the image to the qr_code ImageField
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

    def save(self, *args, **kwargs):
        if not self.qr_code: # Call generate only, if there is no QR code yet
           self.generate_qr_code()
        super().save(*args, **kwargs)