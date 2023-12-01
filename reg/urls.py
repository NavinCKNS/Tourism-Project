from django.urls import path
from django.contrib.auth.decorators import  login_required
from reg import views
from reg.views import show,add
from .views import booked_slots, signup_view,signin_view,home,logout_view,book_slot


urlpatterns = [
    # path('admin/', admin.site.urls),  # Make sure 'admin' namespace is included
    path('about/', views.about),
    path('ap/', views.ap),
    path('signin/',signin_view,name='signin'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
     path('book/', book_slot, name='book_slot'),
     path('booked/', booked_slots, name='booked_slots'),
    path('home/', views.home, name='home'),
    path('ka/', views.ka),
    path('kl/', views.kl),
    path('place/', views.place),
    path('tn/', views.tn),
    path('testimonials/', views.show.as_view(),name='show'),
    path('add/', views.add.as_view(),name="add"),

    # Add other app-specific URL patterns if needed

    # path('', views.signin),
    # path("home/", views.reg, name="home"),
    # path("login/", views.reg, name="login"),
]