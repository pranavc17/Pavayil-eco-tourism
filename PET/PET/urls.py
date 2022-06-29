"""PET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from numpy import insert
from app1 import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login1/', views.login1),
    path('form/', views.form), 
    path('index/', views.index), 
    path('menubar/', views.menubar),
    path('index-page/', views.index_page), 
    path('admin_menu/', views.admin_menu),
    path('add_activity/', views.addactivity),
    # path('reg_form/', views.reg_form),
    path('addactivity1/', views.addact),
    path('activity_table/', views.activity_table),
    path('remove_activity/<str:id1>',views.removeactivity),
    path('view_act_table/', views.viewacttable),
    path('add_resort/', views.addresort),
    path('addresort2/', views.addresortaction),
    path('resort_table/', views.resort_table),
    path('remove_resort/<str:id1>', views.removeresort),
    path('view_res_table/', views.viewrestable),
    path('add_homestay/', views.addhomestay),
    path('addhomestay2/', views.addhomestayaction),
    path('homestay_table/', views.homestay_table),
    path('remove_homestay/<str:id1>', views.removehomestay),
    path('view_hom_table/', views.viewhomtable),
    path('publicview/', views.publicview),
    path('justview/', views.justview),
    path('sample/', views.sample),
    path('log/',views.log),
    path('resort_menu/',views.resort_menu),
    path('homestay_menu/',views.homestay_menu),
    path('loginlink/',views.loginlink),
    path('editresort/',views.editresort),
    path('editresort2/<str:id1>',views.editresort2),
    path('edithomestay/',views.edithomestay),
    path('trav_activity/',views.trav_activity),
    path('trav_resort/',views.trav_resort),
    path('trav_homestay/',views.trav_homestay),
    path('trav_menu/',views.trav_menu),
    path('addtraveller/',views.addtraveller),
    path('addtravelleraction/',views.addtravelleraction),
    path('homestaybooking/<str:id1>',views.homestaybooking),
    path('homestaybookingaction/',views.homestaybookingaction),
    path('resortbooking/<str:id1>',views.resortbooking),
    path('resortbookingaction/',views.resortbookingaction),
    path('activitybooking/<str:id1>',views.activitybooking),
    path('activitybookingaction/',views.activitybookingaction),
    path('viewactivitybooking1/',views.viewactivitybkselect),
    path('viewactivitybooking1action/',views.viewactivitybookingbooking1action),
    path('acceptact/<str:id>',views.acceptact),
    path('rejectact/<str:id>',views.rejectact),
    path('viewresortbooking/',views.viewresortbooking),
    path('acceptres/<str:id>',views.acceptres),
    path('rejectres/<str:id>',views.rejectres),
    path('viewhomestaybooking/',views.viewhomestaybooking), 
    path('accepthom/<str:id>',views.accepthom),
    path('rejecthom/<str:id>',views.rejecthom),
    path('justviewhomestaybooking/',views.justviewhomestaybooking),
    path('justviewresortbooking/',views.justviewresortbooking),
    path('activityresponse/',views.actresponse),
    path('resortresponse/',views.resresponse),
    path('homestayresponse/',views.homresponse),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
