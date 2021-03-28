from django.shortcuts import render
def renderHomepage(request):
    return render(request,'index.html')