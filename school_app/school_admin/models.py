from django.db import models

# Create your models here.
class SchoolAdmin(models.Model):
    admin_id = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)
     
    class Meta:
        db_table = "school_admin"