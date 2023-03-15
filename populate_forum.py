import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					 'hearmeout_forum.settings')

import django
django.setup()
from forum.models import Category, Post

def populate():
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.
	
	music_posts = [
		{'topic': 'Afrobeats is Goated',
		 'comment':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
		 'likes':123},
		{'topic':'Kanye West is a top Artist',
		 'comment':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
		 'likes':70},
		{'topic':'Kpop is overrated',
		 'comment':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur',
		 'likes':95} ]
	
	movies_posts = [
		{'topic':'Journey to the West',
		 'comment':'ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',
		 'likes':1},
		{'topic':'Bad Boys',
		 'comment':'ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',
		 'likes':13},
		{'topic':'The Avengers',
		 'comment':'ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',
		 'likes':21} ]
	
	arts_posts = [
		{'topic':'Dogs',
		 'comment':'ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',
		 'likes':25},
		{'topic':'Cats',
		 'comment':'ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo',
		 'likes':59} ]
	
	food_pages=[]

	
	cats = {'Music': {'posts': music_posts,'engagements':70},
			'Movies': {'posts': movies_posts,'engagements':64},
			'Arts':{'posts':arts_posts,'engagements':50},
			'Food':{'posts':food_pages, 'engagements':60},
			}
	
	# If you want to add more categories or pages,
	# add them to the dictionaries above.
	
	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated pages for that category.
	for cat, cat_data in cats.items():
		c = add_cat(cat,cat_data['engagements'])
		for p in cat_data['posts']:
			add_page(c, p['topic'], p['comment'],p['likes'])
	
	# Print out the categories we have added.
	for c in Category.objects.all():
		for p in Post.objects.filter(category=c):
			print(f'- {c}: {p}')

def add_page(cat, topic, comment, likes):
	p = Post.objects.get_or_create(category=cat, topic=topic)[0]
	p.comment= comment
	p.likes=likes
	p.save()
	return p

def add_cat(name,engagements):
	c = Category.objects.get_or_create(name=name,engagements=engagements)[0]
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print('Starting Rango population script...')
	populate()