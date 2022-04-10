from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length= 10)
    birth_date = models.DateField()
    phone = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.last_name}  {self.name} - {self.birth_date} - {self.phone}"

