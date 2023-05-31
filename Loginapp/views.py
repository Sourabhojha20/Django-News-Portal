from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
# Create your views here.
def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            request.session['uid']=username
            
            return redirect('Dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('Userlogin')
    return render(request, 'LoginForm.html')

def Logout(request):
    if request.method == 'POST':
        request.session.flush() # deletes session data and creates new empty session
        request.session.clear_expired() # deletes all expired sessions
        logout(request)
        
    return redirect('Userlogin')