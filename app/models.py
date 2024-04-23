from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    status_choices=[
        ('C','COMPLETED'),
        ('P','PENDING')
    ]

    priority_choices=[
        ('1','ONE'),
        ('2','TWO'),
        ('3','THREE'),
        ('4','FOUR'),
        ('5','FIVE'),
        ('6','SIX'),
        ('7','SEVEN'),
        ('8','EIGHT'),
        ('9','NINE'),
        ('10','TEN'),
            
    ]



    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2,choices=status_choices)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=2,choices=priority_choices)


