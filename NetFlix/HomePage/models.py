from statistics import mode
from django.db import models

# Create your models here.

class Destination(models.Model):
    dest_pk = models.AutoField(primary_key=True)
    dest_name = models.TextField(max_length=30)
    num_days = models.IntegerField()
    num_price = models.IntegerField()
    TRANS_MODE = (
        ('R', 'Road'),
        ('A', 'Air'),
        ('W', 'Water'),
    )
    mode_of_travel = models.CharField(max_length=1, choices=TRANS_MODE)
    # mode_of_travel = models.CharField(choices=('Land', 'Water','Air'))
    spots_covered = models.TextField(max_length=150)

    def __str__(self):
        return self.dest_name

# user -
# Full name - txt 50 
# email address - emailfield
# mobile number - int 
# username pass - txt
class UserCust(models.Model):
    usercust_pk = models.AutoField(primary_key=True)
    full_name = models.TextField(max_length=50)
    email_add = models.EmailField(unique=True)
    mobile_num = models.IntegerField()
    user_pass = models.CharField(max_length=10)


