from django.db import models
class INSTITUTE_ADMITTED(models.Model):
    pass

class NON_INSTITUTE_ADMITTED(models.Model):
    
    created_at = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    reason=  models.CharField(max_length= 100)
    phone = models.IntegerField()
    vehicle_no = models.CharField(max_length=10)
    
    

