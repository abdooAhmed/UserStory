from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('list/', views.userStoryVersions_list, name='userStoryVersions'),
    path('addUserStoryVersion/', views.add_userStoryVersions,
         name='addUserStoryVersion'),
    path('userStoryVersionDetails/<int:id>',
         views.userStoryVersionDetails, name='userStoryVersionDetails')
]
