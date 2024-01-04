from .models import User,Profile
from django.db.models.signals import post_save,post_delete
def createProfile(sender,instance,created,**kwargs): 
    if created: 
        user=instance 
        profile=Profile.objects.create(user=user,
                                       username=user.username, 
                                       email=user.email, 
                                       name=user.first_name) 
post_save.connect(createProfile,sender=User)  

def deleteUser(sender,instance,**kwargs): 
    user=instance.user 
    user.delete() 
post_delete.connect(deleteUser,sender=Profile) 
