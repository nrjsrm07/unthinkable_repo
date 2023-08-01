from django.db import models
from django.core.validators import RegexValidator

password_regex = RegexValidator(
    regex=r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).{8,}$",
    message=(
        "Password must contain at least one uppercase letter, "
        "one lowercase letter, one special character (@#$%^&+=!), "
        "one numeric digit, and be at least 8 characters long."
    ),
)

username_regex = RegexValidator(
    regex=r"^[a-zA-Z0-9]*$", message=("Only alphanumeric username is allowed.")
)


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True, validators=[username_regex])
    password = models.CharField(max_length=128, validators=[password_regex])
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profession = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username
