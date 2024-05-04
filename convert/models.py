from django.db import models

class Files(models.Model):
    pdf = models.FileField(upload_to='pdf/')
