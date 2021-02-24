from django.urls import path
from . import views


urlpatterns=  [
    path('',views.homepage,name="homepage"),
    path('classes',views.handleClasses,name="handleClasses"),
    path('teaching',views.handleTeaching,name="handleTeaching"),
    path('signup',views.handleSignUp,name="handleSignUp"),
    path('login',views.handleLogIn,name="handleLogIn"),
    path('logout',views.handleLogOut,name="handleLogOut"),
    path('create-class',views.handleCreateClass,name="handleCreateClass"),
    path('join-class',views.handleJoinClass,name="handleJoinClass"),
    path('update-profile',views.handleUpdateProfile,name="handleUpdateProfile"),
    path('profile',views.profile,name="profile"),
    path('teaching/<str:slug>',views.insertTeachingClass,name="insertTeachingClass"),
    path('change-profile-pic',views.changeProfilePic,name="changeProfilePic"),
]