from django.urls import path
from .views import home,create_Donation,donation_list,delete,edit,Signup,Login,Logout,UserProfile

urlpatterns = [
    path('home/',home,name="home"),
    path('creates/',create_Donation,name="create"),
    path('list/',donation_list,name="list"),
    path('edit/<int:id>/',edit,name="edit"),
    path('delete/<int:id>/',delete,name="delete"),
    path('signup/',Signup,name="signup"),
    path('login/',Login,name="user_login"),
    path('logout/',Logout,name="user_logout"),
    path('profile/',UserProfile,name="user_profile"),
] 