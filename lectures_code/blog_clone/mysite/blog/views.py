# Import get_object_or_404() for add comment section
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
#import mixins and decorators
from django.contrib.auth.mixins import LoginRequiredMixin   #used for class based views
from django.contrib.auth.decorators import login_required    #used for functions

# Create your views here.
#########################################################
###################################################
# post views

# create first about page
class AboutView(TemplateView):
    template_name='about.html'

# returns post_list by default or else what we want using context_
class PostListView(ListView):
    model=Post

    def get_queryset(self):
        # __lte is stands for <=
        # -published_date dash means desending order
        #documentation is present https://docs.djangoproject.com/en/1.10/topics/db/queries
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post

#we only want it to be created by superuser so we use mix-ins
class CreatePostView(LoginRequiredMixin,CreateView):
    #  there are 2 Attribute for mixins
    # where shoudl go after login
    login_url='/login/'
    #redirect to detail view
    redirect_field_name='blog/post_detail.html'
    #--------
    form_class=PostForm
    model=Post

class PostUpdateVeiw(LoginRequiredMixin,UpdateView):
    #same as above
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    #--------
    form_class=PostForm
    model=Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list') #post_list is from blog.urls

#same is post list view but without contraint of publication date
class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date') #assending order




######################################################################
#####################################################################
#publish view
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)







##############################################
###########################################

# comment views

@login_required
def add_comment_to_post(request,pk):
    # pk so that comment is specific to a single post
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post #since comment has foriegn key in model
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)


































#######################
