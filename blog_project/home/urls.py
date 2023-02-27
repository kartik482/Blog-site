from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="BLOGSite Admin"
admin.site.site_title="BLOGSite Admin Panel"
admin.site.index_title="Welcome to BLOGSite Admin Panel"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('search/',views.search,name="search"),
    path('signup/',views.handlesignup,name="handlesignup"),
    path('login/',views.handlelogin,name="handlelogin"),
    path('logout/',views.handlelogout,name="handlelogout"),
]