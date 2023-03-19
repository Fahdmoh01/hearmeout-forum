from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from forum.models import Category,Post,UserProfile
from forum.forms import PostForm,UserProfileForm
# Create your views here.

class IndexView(View):
	def get(self, request):
			context_dict={}
			category_list = Category.objects.all()
			post_list = Post.objects.order_by('-likes')[:5]

			context_dict['posts'] = post_list
			context_dict['categories'] = category_list
			context_dict['about']='We out here fighting for our lives!'
			
			
			return render(request, 'forum/index.html/', context= context_dict)
	


class ShowCategoryView(View):
	 
	context_dict= {}
	# @method_decorator(login_required)
	def get(self, request, category_name_slug):
		try:
			category = Category.objects.get(slug = category_name_slug)
			posts = Post.objects.filter(category=category)
			ordered_posts  = posts.order_by('-likes')
			print(ordered_posts)
			self.context_dict['posts'] = ordered_posts
			self.context_dict['category'] = category
		except Category.DoesNotExist:
			self.context_dict['category'] = None
			self.context_dict['posts'] = None

		return render(request, 'forum/category.html', self.context_dict)
	


class AddPostView(View):
	def get(self, request, category_name_slug):
		try:
			category = Category.objects.get(slug = category_name_slug)
		except Category.DoesNotExist:
			category = None
		
		#if cannot add post to a category, it doesn't exist. reload to index page
		if category is None:
			return redirect('/forum/')
		
		form = PostForm()
		context_dict ={'form':form, 'category': category}
		return render(request, 'forum/add_post.html', context= context_dict)
	

	def post(self, request, category_name_slug):
		try:
			category = Category.objects.get(slug = category_name_slug)
		except Category.DoesNotExist:
			category = None

		#You cannot add a page to a Category that does not exist...
		if category is None:
			return redirect('/forum/')
		
		form = PostForm(request.POST)

		if form.is_valid():
			if category:
				post = form.save(commit = False)
				post.category = category
				post.likes =  0
				post.save()

				return redirect(reverse('forum:show_category', kwargs={'category_name_slug': category_name_slug}))
		else:
			print(form.errors)
		
		context_dict ={'form': form, 'category': category}
		return render(request, 'forum/add_post.html', context=context_dict)
	


class RegisterProfileView(View):
	def get(self, request):
		form = UserProfileForm()
		context_dict = {'form': form }
		return render(request, 'forum/profile_registration.html', context_dict)
	
	def post(self, request):
		form = UserProfileForm(request.POST, request.FILES)

		if form.is_valid():
			user_profile = form.save(commit=False)
			user_profile.user = request.user
			user_profile.save()

			return redirect(reverse('forum:index'))
		
		else:
			print(form.errors)

		context_dict = {'form': form }
		return render(request, 'forum/profile_registration.html', context_dict)
	

# class ProfileView(View):
# 	def get_user_details(self, username):
# 		try:
# 			user  = User.objec