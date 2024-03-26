from django.urls import path
from . import views

urlpatterns = [
  path('todos/', views.TodoListCreate.as_view()),
  path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
  path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
  path('signup/', views.signup),
  path('signuptab/', views.signuptab),
  path('login/', views.login),
  path('gettable/', views.gettable),  
  
]
