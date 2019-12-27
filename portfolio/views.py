from django.shortcuts import render

# Create your views here.

def index(request):
    # all_agencies = Agency.objects.all()
    return render(request, 'index.html', locals())