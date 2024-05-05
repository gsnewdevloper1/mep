from django.db import models

# Create your models here.

class pending_work(models.Model):
    sno = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50 , null=False)
    desc = models.CharField(max_length=100 , null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    

class work_details(models.Model):
    sno_com = models.ForeignKey(pending_work,on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.desc
    

class contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name