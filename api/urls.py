from django.urls import path
from .views import UserView,UserDetail, ClientView, ClientDetail,AuthUserRegistrationView,UserLoginView

urlpatterns  = [
	path('users/',UserView.as_view()),
	path('users/<int:pk>/',UserDetail.as_view()),

	path('clients/',ClientView.as_view()),
	path('clients/<int:pk>/',ClientDetail.as_view()),
	path('register/',AuthUserRegistrationView.as_view()),
	path('login/',UserLoginView.as_view()),
	]