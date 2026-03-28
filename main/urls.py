from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('post/<int:post_id>/', views.post_detail, name='post_detail'),
	path('register/', views.register, name='register'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
]
