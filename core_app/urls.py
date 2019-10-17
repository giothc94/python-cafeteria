from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('store/', views.store,name="store"),
    path('contact/', views.contact,name="contact"),
]