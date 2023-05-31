from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.db.models import Count
from django.shortcuts import render,HttpResponse,redirect
from AdminFile.models import News,Advertisement,AddBanner,AddVideo,AajKaRashifal
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    

    MadhyaPradesh=News.objects.filter(category='मध्यप्रदेश')[:5]
    DeshVidesh = News.objects.filter(category='देश-विदेश')[:5]
    Mahanagar = News.objects.filter(category='महानगर')[:5]
    khel = News.objects.filter(category='खेल')[:5]
    Vyapar = News.objects.filter(category='व्यापार')[:5]
    Cinema = News.objects.filter(category='टीवी मूवी')[:5]
    Aadhyatm = News.objects.filter(category='अध्यात्म')[:5]
    Feature = News.objects.filter(category='फ़ीचर')[:5]
    banner=AddBanner.objects.all()
    pd=News.objects.all()
    add=Advertisement.objects.all()
    

    context = {
        
        'feature':Feature,
        'MadhyaPradesh':MadhyaPradesh,
        "DeshVidesh":DeshVidesh,
        "Mahanagar":Mahanagar,
        'khel':khel,
        'Vyapar':Vyapar,
        'Cinema':Cinema,
        'Aadhyatm':Aadhyatm,
        'banner':banner,
        'add':add,
        'news':pd,
        


    }
    return render(request,'index.html',context)


def SinglePost(request):
    return render(request,'single-post.html')

def MadhyaPradesh(request):
    add=Advertisement.objects.all()
    MadhyaPradeshNews=News.objects.filter(category='मध्यप्रदेश')
    paginator = Paginator(MadhyaPradeshNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    MadhyaPradesh= paginator.get_page(page_number)
    context={
        'MadhyaPradesh':MadhyaPradesh,
        'add':add
    }
    return render(request,'MadhyaPradesh.html',context)

def DeshVidesh(request):
    add=Advertisement.objects.all()
    DeshVideshNews = News.objects.filter(category='देश-विदेश')
    paginator = Paginator(DeshVideshNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    DeshVidesh= paginator.get_page(page_number)
    context={
        "DeshVidesh":DeshVidesh,
        'add':add
    }
    return render(request,'DeshVidesh.html',context)

def Mahanagar(request):
    add=Advertisement.objects.all()
    MahanagarNews = News.objects.filter(category='महानगर')
    paginator = Paginator(MahanagarNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    Mahanagar= paginator.get_page(page_number)
    context={
        "Mahanagar":Mahanagar,
        'add':add
    }
    return render(request,'Mahanagar.html',context)

def Khel(request):
    add=Advertisement.objects.all()
    khelNews = News.objects.filter(category='खेल')
    paginator = Paginator(khelNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    khel= paginator.get_page(page_number)
    context={
        'khel':khel,
        'add':add
    }
    return render(request,'Khel.html',context)

def Vyapar(request):
    add=Advertisement.objects.all()
    VyaparNews = News.objects.filter(category='व्यापार')
    paginator = Paginator(VyaparNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    Vyapar= paginator.get_page(page_number)
    context={
        'Vyapar':Vyapar,
        'add':add
    }
    return render(request,'Vyapar.html',context)

def Manoranjan(request):
    add=Advertisement.objects.all()
    CinemaNews = News.objects.filter(category='टीवी मूवी')
    paginator = Paginator(CinemaNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    Cinema= paginator.get_page(page_number)
    context={
        'Cinema':Cinema,
        'add':add
    }
    return render(request,'Manoranjan.html',context)

def Aadhyatm(request):
    add=Advertisement.objects.all()
    AadhyatmNews = News.objects.filter(category='अध्यात्म')
    paginator = Paginator(AadhyatmNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    Aadhyatm= paginator.get_page(page_number)
    context={
        'Aadhyatm':Aadhyatm,
        'add':add
    }
    return render(request,'Aadhyatm.html',context)

def Feature(request):
    add=Advertisement.objects.all()
    FeatureNews = News.objects.filter(category='फ़ीचर')
    paginator = Paginator(FeatureNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    Feature= paginator.get_page(page_number)
    context={
        'feature':Feature,
        'add':add
    }
    return render(request,'Feature.html',context)
    

def Video(request):
    add=Advertisement.objects.all()
    videoNews=AddVideo.objects.all()
    paginator = Paginator(videoNews, 4) # 10 items per page
    page_number = request.GET.get('page')
    video= paginator.get_page(page_number)
    context={
            'videos':video,
        'add':add
    }
    return render(request,'Video.html',context)


def MashikPatrika(request):
    return render(request,'MashikPatrika.html')
# .............................................---------------------------------------------------------------

def test(request):
    mp_count = News.objects.filter(category='मध्यप्रदेश').count()
    khel_count = News.objects.filter(category='खेल').count()
    item=AddVideo.objects.all()
    context={
 
            "mp_count":mp_count,
            "khel_count":khel_count,
            'item':item
    }
    return render(request,'test.html',context)

def Detailview(request,id):
    n=News.objects.get(id=id)
    
    context={
        'news':n,
        
    }
    return render(request,'Detailview.html',context)