from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
# Create your models here.

#main author(super user in this case create a post like facebook we do)
#thi would be post model
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)# only one user(superuser) is using that
    title=models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    # publish date
    def publish(self):
        self.published_date = timezone.now()
        self.save()


#author would aprove if comments is good
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)#approved_comment is same from comment model


#where should the page go after creathing the post
#go to that post's details page (use of reverse)
#post_detail is from detailView in views.py
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


#some other guy comments on my post(since i m superuser) )
#this would be comment model
class Comment(models.Model):
    post= models.ForeignKey('blog.Post',related_name='comments', on_delete = models.CASCADE)#connecting commentto Post
    author = models.CharField(max_length=200)#auther is not same as above :its the commenting author
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)


#for aprove button
    def approve(self):
        self.approved_comment=True
        self.save()

#go to home page(where all posts are) after commenting is done
#post_list is from listView in views.py
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
