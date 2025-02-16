from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=50, default="Basic Visit")  # For MVP
    qr_code = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Changed: Store QR code as text
    notes = models.TextField(blank=True, null=True)
    contact_person_first_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_person_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_person_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def generate_qr_code(self):
        """Generates and saves a QR code containing the client's ID."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(self.id))  # Store the client's ID as a string
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_code = str(self.id) # Save the ID as the qr_code value


    def save(self, *args, **kwargs):
        """Overrides the save method to generate QR code before saving."""
        if not self.qr_code:  # Generate only if it doesn't exist yet
            self.generate_qr_code()
        super().save(*args, **kwargs)