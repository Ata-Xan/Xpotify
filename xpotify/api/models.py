from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import string
import random
def generate_unique_code():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if not Room.objects.filter(code=code).exists():
            return code


class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True, editable=False)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

   
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        super(Room, self).save(*args, **kwargs)


    def clean(self):
        # Ensure code is all uppercase
        self.code = self.code.upper()

        # Ensure code is ASCII
        try:
            self.code.encode('ascii')
        except UnicodeEncodeError:
            raise ValidationError("Code must be ASCII")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Room {self.code} (hosted by {self.host})"

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])
