from django import forms
from forum.models import Post, Category,UserProfile

from django.contrib.auth.models import User

#Meta: describes additional attributes about the class
class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=Category.NAME_MAX_LENGTH, help_text='Please enter the category name.')
	engagements = forms.IntegerField(widget=forms.HiddenInput(),initial = 0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	#An inline class to provide additional information on the form.
	class Meta:
		#Provide an association betwen the ModelForm and a model
		model = Category
		fields = ('name',)


class PostForm(forms.ModelForm):
	topic = forms.CharField(max_length=Post.TOPIC_MAX_LENGTH, label='topic',widget=forms.TextInput(attrs={'placeholder': 'your topic'}))
	comment = forms.CharField(label='comment', widget=forms.Textarea(attrs={'placeholder': 'your comment', 'size': 20}))
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)

	class Meta:
		#Provide association between a the ModelForm and a model
		model = Post
		#What fields do we want to include in our form?
		#This way we don't need every field in the model present
		#Some fields may allow NULL values; we may not want to include them.
		#Here, we are hiding the foreign key
		#we can either exclude the category field from the form,
		
		exclude =('category',)
		#or specify the fields to include (don't include the category field).


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		#fields indicate which fields on the model should be present when form has been successfully rendered
		fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		#fields indicate which fields on the model should be present when form has been successfully rendered
		fields = ('picture',)
