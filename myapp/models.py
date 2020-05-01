from django.db import models


from django.conf import settings
from django.contrib.auth.models import User,auth
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nicname=models.CharField(blank=True,max_length=100)
    Phoneno=models.CharField(blank=True,max_length=10)

    Adres=models.TextField(blank=True)

    def __str__(self):
        return self.user.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class Image(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Image =models.URLField(blank=True, default='pro.jpeg')

    def __str__(self):
        return self.Image
def create_profil(sender,**kwargs):
    if kwargs['created']:
        user_image=Image.objects.create(user=kwargs['instance'])
post_save.connect(create_profil,sender=User)

class Image2(models.Model):
    Image=models.ImageField(blank=True,null=True,default='pro.jpeg')
    def __str__(self):
        return self.Image.url

class Blog(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    pro=models.URLField(blank=True,default='pro.jpeg')
    Title=models.CharField(max_length=200,blank=False)
    Image=models.URLField(blank=True)
    Contents=models.TextField(blank=True)
    Date=models.DateTimeField(auto_now_add=True)
    likeno=models.CharField(max_length=200,blank=0,default=0)
    commtno=models.CharField(max_length=200,blank=0,default=0)




    def __str__(self):
        return self.Title
    def __unicode__(self):
        return u'%s' % self.Title


class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    post=models.ForeignKey(Blog,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    pic=models.URLField(default='pro.jpeg')
    def __str__(self):
        return self.user.username
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

