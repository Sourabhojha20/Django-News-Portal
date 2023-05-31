from django.contrib import admin
from django.urls import path
from AdminFile import views

urlpatterns = [
    path('home',views.Dashboard,name='Dashboard'),
    path('ViewCategory/',views.ViewCategory,name='ViewCategory'),
    path('AddNews/',views.AddNews,name='AddNews'),
    path('ViewAllNews/',views.ViewAllNews,name='ViewAllNews'),
    path('Newsupdate/<int:id>',views.Newsupdate,name="Newsupdate"),
    path('Newsedit/<int:id>',views.Newsedit,name="Newsedit"),
     path('Newsdelete/<str:id>/',views.Newsdelete,name="Newsdelete"),
    path('Newsheadlinestatus/<int:id>',views.HeadlineStatus,name='NewsHeadlineStatus'),
    path('Newshomestatus/<int:id>',views.HomeStatus,name='NewsHomeStatus'),
    path('BannerNews/',views.BannerNews,name='BannerNews'),
    path('Addbanner/',views.Addbanner,name='Addbanner'),
    path('Bannerupdate/<int:id>',views.Bannerupdate,name="Bannerupdate"),
    path('Banneredit/<int:id>',views.Banneredit,name="Banneredit"),
    path('Bannerdelete/<str:id>/',views.Bannerdelete,name="Bannerdelete"),
    path('Bannerstatusupdate/<int:id>',views.BannerStatusUpdate,name="statusupdate"),
    path('VideosNews/',views.VideosNews,name='VideosNews'),
    path('Addvideo/',views.Addvideo,name='Addvideo'),
    path('videostatusupdate/<int:id>',views.VideoStatusUpdate,name="videostatusupdate"),
    path('MashikPatrika/',views.AllMashikPatrika,name='AllMashikPatrika'),
    path('AddPatrika/',views.AddPtrika,name='AddPatrika'),
    
    path('SubAdmin/',views.SubAdmin,name='SubAdmin'),
    path('SubAdminList/',views.SubAdminList,name='SubAdminList'),
    path('AllAdvertisement/',views.AllAdvertisement,name='AllAdvertisement'),
    path('AddAdvertisement/',views.AddAdvertisement,name='AddAdvertisement'),
    path('ADDupdate/<int:id>',views.ADDupdate,name="ADDupdate"),
    path('ADDedit/<int:id>',views.ADDedit,name="ADDedit"),
    path('ADDdelete/<str:id>/',views.ADDdelete,name="ADDdelete"),
    path('AajKaRashiFal/',views.AajKaRashiFal,name='AajKaRashiFal'),
    path('tst',views.tst),
    # path('view_pdf/<int:pk>/', views.view_pdf, name='view_pdf'),
    # path('pdf_view',views.view_pdf, name='view_pdf'),
    path('pdfs/<int:pk>/', views.pdf_view, name='pdf_view'),
]
