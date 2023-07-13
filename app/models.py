from django.db import models


class Hotel(models.Model):
    c = (('1',"Marriot"),('2',"Rixos"),('3',"Sheraton"),('4',"St Regis"),('5',"Radison"),('6',"Ritz"))
    
    name = models.CharField(max_length=100, choices=c, null=False)
    
    def __str__ (self):
        return self.name
