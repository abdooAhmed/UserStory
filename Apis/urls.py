from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('removeUserStory/<int:id>', views.del_userStroy, name='del'),
    path('relatedUserStory',
         views.related_userStory, name='relatedUserStories')
]
