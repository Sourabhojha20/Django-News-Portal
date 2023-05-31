from AdminFile.models import News,AajKaRashifal,Advertisement

def base(request):
    mp_count = News.objects.filter(category='मध्यप्रदेश').count()
    khel_count = News.objects.filter(category='खेल').count()
    desh_videsh_count = News.objects.filter(category='देश-विदेश').count()
    mahanagar_count = News.objects.filter(category='महानगर').count()
    vyapar_count = News.objects.filter(category='व्यापार').count()
    tv_movie_count = News.objects.filter(category='टीवी मूवी').count()
    adhyatam_count = News.objects.filter(category='अध्यात्म').count()
    feature_count = News.objects.filter(category='फ़ीचर').count()
    Rashi=AajKaRashifal.objects.all().last()
    khel = News.objects.filter(category='खेल')[:5]
    Feature = News.objects.filter(category='फ़ीचर')[:5]
    add=Advertisement.objects.all()
    context={
        "mp_count": mp_count,
        "khel_count": khel_count,
        "desh_videsh_count": desh_videsh_count,
        "mahanagar_count": mahanagar_count,
        "vyapar_count": vyapar_count,
        "tv_movie_count": tv_movie_count,
        "adhyatam_count": adhyatam_count,
        "feature_count": feature_count,
        'Rashi':Rashi,
        'khel':khel,
        'feature':Feature,
        'add':add,
    }
    return (context)

