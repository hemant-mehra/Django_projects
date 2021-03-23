from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields=('author','title','text')
#creating widgets to give more bootstrap feels to fields  then defalut like last examples
        widgets = {
            #textinputclass for  our css use
            'title':forms.TextInput(attrs={'class':'textinputclass'}),

            #editable medium-editor-textarea is from bootstarp to gie feel same as medium.com
            # postcontent for our CSS use
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields=('author','text')

        #same as above
        widgets={
            'auther':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }
