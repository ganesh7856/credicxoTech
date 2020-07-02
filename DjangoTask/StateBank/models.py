from django.db import models

# Create your models here.

class Branch_Name(models.Model):
    bank = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=256,null=False)
    ifsc_code = models.CharField(max_length=500, unique=True,null=False)
    address = models.TextField()
    city = models.CharField(max_length=500,null=False)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)


    def __str__(self):
        return "{},{},{}".format(self.bank,self.branch_name, self.city)
