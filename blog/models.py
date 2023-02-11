from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class Post(models.Model):
    aurthur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    date_created = models.DateTimeField(blank=False, auto_now_add=True)

    def __str__(self):
        return f"{self.aurthur} {self.text}"

class Document(models.Model):
    document = models.FileField(upload_to="uploads/", validators=[FileExtensionValidator(["pdf", "jpg", "jpeg", "png", "gif"])])
    aurthur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # hashes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.aurthur} --> {self.document}'