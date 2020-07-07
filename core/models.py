from django.db import models

class usuario(models.Model):

    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    number = models.CharField(max_length=9)
    complement = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=8)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)

    class meta:
        db_table = 'Address'
