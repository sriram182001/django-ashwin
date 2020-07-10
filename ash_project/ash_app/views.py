from django.shortcuts import render
from ash_app.forms import FormPhoto
# Create your views here.
def index(request):
    form= FormPhoto()
    if request.method=="POST":
        form= FormPhoto(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            print("valid form")
            #if 'user_pic'in request.FILES:
                #form.user_pic=request.FILES['user_pic']
            #form.save(commit=True)
        else:
            print("invalid form")
    return render(request,'index.html',{'form':form})
