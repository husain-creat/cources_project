from django.shortcuts import render,redirect,HttpResponse
from .models import cource
from django.contrib import messages

def index(request):
    if request.method =='POST':
        errors = cource.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:

            cource.objects.create(
                name = request.POST['name'],
                description = request.POST['description']
            )
    context={
        "all_cources":cource.objects.all()
    } 
    return render(request,'cources.html',context) 
def destroy(request,id):
     cource_del= cource.objects.get(id = id)
     context = {
        "cource_del":cource_del
    }
     return render(request,'destroy.html',context)



def delete(request,id):
    course_delete = cource.objects.get(id = id)
    course_delete.delete()
    
    return redirect('/')
