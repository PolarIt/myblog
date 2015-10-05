from django import forms

class BlogForm(forms.Form):
	title = forms.CharField(label='title',max_length=100)
	content = forms.CharField(widget=forms.Textarea)

class TagForm(forms.Form):
    tag_name = forms.CharField()