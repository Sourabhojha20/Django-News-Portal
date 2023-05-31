from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, get_object_or_404
from datetime import datetime
# Create your views here.
from django.db.models import Count
from django.shortcuts import render,HttpResponse,redirect
from AdminFile.models import News,Advertisement,AddBanner,AddVideo,AddMashikPatrika,AajKaRashifal,CustomUser
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url='Userlogin')
def Dashboard(request):
    news=News.objects.all()[:15]
    cdata=News.objects.all().count()
    advertisement=Advertisement.objects.all()
    cAdd=Advertisement.objects.all().count()
    category_counts = News.objects.values('category').annotate(total=Count('category'))
    c_count = len(category_counts)
    context={
        'news':news,
        'add': advertisement,
        'cdata':cdata,
        'cAdd':cAdd,
        'c_count':c_count
    }
    return render(request,'DashBoard.html',context)

@login_required(login_url='Userlogin')
def ViewCategory(request):
    return render(request,'ViewCategory.html')

@login_required(login_url='Userlogin')
def AddNews(request):
    if request.method=='POST':
        title=request.POST.get('pt_title')
        category=request.POST.get('pt_category')
        image=request.FILES.get('pt_image')
        description=request.POST.get('pt_description')
        tags=request.POST.get('pt_tags')
        status=request.POST.get('pt_status')
        b=News.objects.create(title=title, description=description, category=category, image=image, tags=tags, status=status, created_at=datetime.now())
        b.save()
        messages.success(request,'News added succefully')
        return redirect('AddNews')
    return render(request,'AddNews.html')

@login_required(login_url='Userlogin')
def ViewAllNews(request):
    allnews=News.objects.all()
    paginator = Paginator(allnews, 10) # 10 items per page
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    context={
        # 'news':news,
        'news': news
    }
    return render(request,'ViewAllNews.html',context)

@login_required(login_url='Userlogin')
def Newsupdate(request,id):
    edit=News.objects.get(id=id)
    return render(request, 'Newsupdate.html', {'edit': edit})

@login_required(login_url='Userlogin')
def Newsedit(request,id):
    update = News.objects.get(id=id)
    if request.method == 'POST':
        update.title = request.POST['pt_title']
        update.description = request.POST['pt_description']
        update.image = request.FILES.get('pt_image')
        update.category = request.POST.get('pt_category')
        update.status=request.POST.get("pt_status")
        update.tags=request.POST.get('pt_tags')
        update.save()
        messages.success(request,'News updated successfully')
    return redirect('ViewAllNews')

@login_required(login_url='Userlogin')   
def Newsdelete(request,id):
        pi=News.objects.get(id=id)
        pi.delete()
        messages.success(request,'News Deleted successfully')
        return redirect('ViewAllNews')

@login_required(login_url='Userlogin')
def HomeStatus(request,id):
    obj = News.objects.get(id=id)
    if(obj.show_in_home == 1):
        obj.show_in_home = False
        obj.save()
    else:
        obj.show_in_home = True
        obj.save()
    return  redirect("ViewAllNews")

@login_required(login_url='Userlogin')
def HeadlineStatus(request,id):
    obj = News.objects.get(id=id)
    if(obj.show_in_headline == 1):
        obj.show_in_headline = False
        obj.save()
    else:
        obj.show_in_headline = True
        obj.save()
    return  redirect("ViewAllNews")

@login_required(login_url='Userlogin')
def BannerNews(request):
    news=AddBanner.objects.all()
    context={
        'news':news
    }
    return render(request,'BannerNews.html',context)
@login_required(login_url='Userlogin')
def Addbanner(request):
    if request.method=='POST':
        image=request.FILES.get('pt_image')
        status=request.POST.get('pt_status')
        a=AddBanner.objects.create(image=image,status=status)
        a.save()
        messages.success(request,'Banner added Successfully')
        return redirect('Addbanner')
    return render(request,'AddBanner.html')

@login_required(login_url='Userlogin')
def Bannerupdate(request,id):
    edit=AddBanner.objects.get(id=id)
    return render(request, 'Bannerupdate.html', {'edit': edit})
@login_required(login_url='Userlogin')
def Banneredit(request,id):
    update = News.objects.get(id=id)
    if request.method == 'POST':
        update.image=request.FILES.get('pt_image')
        update.status=request.POST.get('pt_status')
        update.save()
        messages.success(request,'Banner Updated Successfully')
    return redirect('BannerNews')


@login_required(login_url='Userlogin')   
def Bannerdelete(request,id):
        pi=AddBanner.objects.get(id=id)
        pi.delete()
        messages.success(request,'Banner deleted Successfully')
        return redirect('BannerNews')

@login_required(login_url='Userlogin')
def BannerStatusUpdate(request,id):
    obj = AddBanner.objects.get(id=id)
    if(obj.status == 1):
        obj.status = False
        obj.save()
    else:
        obj.status = True
        obj.save()
    return redirect('BannerNews')

@login_required(login_url='Userlogin')
def VideosNews(request):
    videonews=AddVideo.objects.all()
    paginator = Paginator(videonews, 5) # 10 items per page
    page_number = request.GET.get('page')
    video= paginator.get_page(page_number)
    context={
        'video':video
    }
    return render(request,'VideoNews.html',context)

@login_required(login_url='Userlogin')
def Addvideo(request):
    if request.method=='POST':
        title=request.POST.get('pt_title')
        vedio=request.POST.get('pt_videoid')
        status=request.POST.get('pt_status')
        a=AddVideo.objects.create(title=title,status=status,video=vedio)
        a.save()
        messages.success(request,'Video_News added Successfully')
        return redirect('Addvideo')
    return render(request,'AddVideo.html')


@login_required(login_url='Userlogin')
def VideoStatusUpdate(request,id):
    
    obj = AddVideo.objects.get(id=id)
    if(obj.status == 1):
        obj.status = False
        obj.save()
    else:
        obj.status = True
        obj.save()
    return redirect('VideosNews')


@login_required(login_url='Userlogin')
def AllMashikPatrika(request):
    return render(request,'AllPatrika.html')


@login_required(login_url='Userlogin')
def AddPtrika(request):
    if request.method=="POST":
        title=request.POST.get('pt_title')
        image=request.FILES.get('pt_image')
        pdf=request.FILES.get('pt_pdf')
        status=request.POST.get('pt_status')
        a=AddMashikPatrika.objects.create(title=title,image=image,pdf=pdf,status=status)
        a.save
        messages.success(request,'Patrika added Successfully')
    return render(request,'AddPatrika.html')


@login_required(login_url='Userlogin')
def SubAdmin(request):
    if request.method == 'POST':
        username=request.POST.get('users[puser_fullname]')
        email=request.POST.get('users[puser_email]')
        password=request.POST.get('users[puser_password]')
        phoneno=request.POST.get('users[puser_mobile1]')
        status=request.POST.get('users[puser_status]')
        permisions=request.POST.getlist('Permision')
        if len(phoneno) == 10:
            user = CustomUser.objects.create_user(username=username,email=email,password=password,phone_number=phoneno,status=status,permission=permisions)
            user.save()
            messages.success(request,'Successfully created')
            return redirect('SubAdmin')
        else:
            messages.error(request,'The phone number should have ten digits.')
    return render(request,'SubAdmin.html')


@login_required(login_url='Userlogin')
def SubAdminList(request):
    return render(request,'SubAdminList.html')

@login_required(login_url='Userlogin')
def AllAdvertisement(request):
    add=Advertisement.objects.all()
    context={
        'add':add
    }
    return render(request,'AllAdvertisement.html',context)


@login_required(login_url='Userlogin')
def AddAdvertisement(request):
    if request.method == 'POST':
        title = request.POST.get('pt_title')
        ctg = request.POST.get('ctg')
        image = request.FILES.get('pt_image')
        status = request.POST.get('pt_status')
        Advertisement.objects.create(title=title, ctg=ctg, image=image, status=status)
        messages.success(request,'Advertisement added Successfully')
        return redirect('AddAdvertisement')
    return render(request, 'AddAdvertisement.html')

@login_required(login_url='Userlogin')

def ADDupdate(request,id):
    edit=Advertisement.objects.get(id=id)
    return render(request, 'ADDupdate.html', {'edit': edit})

@login_required(login_url='Userlogin')
def ADDedit(request,id):
    update = Advertisement.objects.get(id=id)
    if request.method == 'POST':
        update.title = request.POST['pt_title']
        update.image = request.FILES.get('pt_image')
        update.ctg = request.POST.get('pt_category')
        update.status=request.POST.get("pt_status")
        update.save()
        messages.success(request,'Advertisement updated Successfully')
    return redirect('AllAdvertisement')

@login_required(login_url='Userlogin')    
def ADDdelete(request,id):
        pi=Advertisement.objects.get(id=id)
        pi.delete()
        messages.success(request,'Advertisement deleted Successfully')
        return redirect('AllAdvertisement')

@login_required(login_url='Userlogin')
def AajKaRashiFal(request):
    if request.method == 'POST':
        
        description=request.POST.get('pt_description')
        a=AajKaRashifal.objects.create(description=description)
        a.save()
        messages.success(request,'Rashifal added Successfully')
    return render(request,'AajKaRashiFal.html')

def tst(request):
    
    pd=AddVideo.objects.all()
    
  
    context={

            
            'videos':pd,
            
    }
    return render(request,'tst.html',context)


def pdf_view(request, pk):
    pdf = get_object_or_404(AddMashikPatrika, pk=pk)
    response = HttpResponse(pdf.pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="{}"'.format(pdf.title)
    return response