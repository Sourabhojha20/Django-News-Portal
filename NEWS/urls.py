from django.contrib import admin
from django.urls import path
from NEWS import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    
    
    path('',views.index,name='index'),
    # path('base/',views.base),
    
    path('MadhyaPradesh/',views.MadhyaPradesh,name='MadhyaPradesh'),
    path('DeshVidesh/',views.DeshVidesh,name='DeshVidesh'),
    path('Mahanagar/',views.Mahanagar,name='Mahanagar'),
    path('Khel/',views.Khel,name='Khel'),
    path('Vyapar/',views.Vyapar,name='Vyapar'),
    path('Manoranjan/',views.Manoranjan,name='Manoranjan'),
    path('Aadhyatm/',views.Aadhyatm,name='Aadhyatm'),
    path('Feature/',views.Feature,name='Feature'),
    path('Video/',views.Video,name='Video'),
    path('MashikPatrika/',views.MashikPatrika,name='MashikPatrika'),
    path("test1/",views.test, name="test1"),
    path('Detailview/<str:id>/',views.Detailview,name='Detailview')
]
