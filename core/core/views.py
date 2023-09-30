from django.http import HttpResponse

def test_loggedin(request):
    return HttpResponse('<h1>Hello!</h1>')    

def test_logout(request):
    return HttpResponse('<h1>Goodbye! You are logged out!</h1>')    