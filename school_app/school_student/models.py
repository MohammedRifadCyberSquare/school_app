from django.db import models
import datetime

# Create your models here.
class Notes(models.Model):
    subject = models.CharField()
    date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length = 200)
    added_by = models.CharField(max_length=100)
    student_cls = models.IntegerField()
    file = models.FileField(upload_to="notes/")
     
    status = models.CharField(max_length=20, default = 'active')
    class Meta:
        db_table = "notes"