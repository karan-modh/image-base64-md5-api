from django.db import models


class Image(models.Model):
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.file.name
