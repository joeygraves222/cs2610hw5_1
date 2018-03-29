from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(label='Blog Title:', max_length=100)
    author = forms.CharField(label='Author:', max_length=100)
    content = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):
    nickname = forms.CharField(label='Nickname:', max_length=100)
    email = forms.CharField(label='Email:', max_length=100)
    content = forms.CharField(widget=forms.Textarea)