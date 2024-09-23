from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Create database structure
class Task(models.Model): #database table 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #set many-to-one relationship using ForeignKey
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # Set string representation of model and it's official name
    def __str__(self):
        return self.title

    # Order query set, order by complete status
    class Meta:
        ordering = ['complete']
