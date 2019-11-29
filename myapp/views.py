from django.shortcuts import render

# Create your views here.
def fn_index1( request):
    return render(request,'assign7.html')

def fn_index2(request):
    return render(request,'fb.html')

def fn_index3(request):
    return render(request,'fbhome.html')    