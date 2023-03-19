from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
	path('category/<slug:category_name_slug>/add_post/', views.AddPostView.as_view(), name='add_post'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),

]