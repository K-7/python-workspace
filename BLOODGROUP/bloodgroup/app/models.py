from django.db import models
from django.contrib.auth.models import User
#from reportlab.lib.colors import black
#from reportlab.lib.rparsexml import verbose

class Userprofile(User):
    
    YES_NO_CHOICE_LIST =  (
                            ('y', 'Yes'),
                            ('n', 'No'),
                          )
    
    mobile_number = models.CharField(null=False,max_length=10,verbose_name=(u'Mobile Number'),)
    address = models.TextField(blank=True,null=True,verbose_name=(u'Address'),)
    blood_group = models.CharField(null=False,max_length=10,verbose_name=(u'Blood Group'),)
    availability = models.CharField(choices=YES_NO_CHOICE_LIST,max_length=3,null=False,default=YES_NO_CHOICE_LIST[0][0],verbose_name=(u'Availability'),)
    latitude = models.CharField(blank=True,null=True,max_length=50)
    longitude = models.CharField(blank=True,null=True,max_length=50)
    class Meta:
        db_table = "user_profile"
        
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name