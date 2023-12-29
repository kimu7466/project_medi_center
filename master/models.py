from django.db import models

# Create your models here.
class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

class CounterTable(BaseClass):
    last_staff_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Total staff : {self.last_staff_id}"