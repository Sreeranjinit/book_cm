from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Empform,bookform,itemform,mobileform,studentform
from work.models import emp,item,book,mobilModel,Student
# Create your views here.

class EmpView(View):
    def get(self,request):
        form=Empform()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=Empform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #modelname.objects.create()
            emp.objects.create(**form.cleaned_data)  #database lekk add cehyyan vendi data ye unpack cheyyan ** kodukkunnuu
            form=Empform()
            return render(request,"add.html",{"form":form})
             
        else: 
            return render(request,"add.html",{"form":form}) 
        

class  itemview(View):
    def get(self,request):
        form=itemform()
        return render(request,"item.html",{"form":form})
    def post(self,request):
        form=itemform(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # item.objects.create(**form.cleaned_data)
                            #or
            form.save()
            form=itemform()

            return render(request,"item.html",{"form":form})
        else:
            return render(request,"item.html",{"form":form})


        
class bookview(View):
    def get(self,request):
        form=bookform()
        return render(request,"book.html",{"form":form})
    def post(self,request):
        form=bookform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # book.objects.create(**form.cleaned_data)
                                #or
            form.save()  #method is used to add data into database without using ORM query(only for ModelForm)
            form=bookform()
            return render(request,"book.html",{"form":form})
        else:
            return render(request,"book.html",{"form":form})
  
class booklist(View):
    def get(self,request):
        qs=book.objects.all()
        return render(request,"booklist.html",{"qs":qs})


class bookdetail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=book.objects.get(id=id)
        return render(request,"bookdetail.html",{"qs":qs})

class delbook(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        book.objects.get(id=id).delete()
        return redirect('book-l')           
    
# class mobileview(View):
#     def get(self,request):
#         form=mobileform()
#         return render(request,"mobile.html",{"form":form})
#     def post(self,request):
#         form=mobileform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # mobilModel.objects.create(form.cleaned_data)
#             form.save()
#             form=mobileform()
#             return render(request,"mobile.html",{"from":form})
#         else:
#             return render(request,"mobile.html",{"form":form})
        
        
# class mobilelist(View):
#     def get(self,request):
#         s=mobilModel.objects.all()
#         return render(request,"mobilelist.html",{"s":s})
    

# class getmobile(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("id")
#         s=mobilModel.objects.get(id=id)
#         return render(request,"getmobi.html",{"s":s})


class studentview(View):
    def get(self,request):
        form=studentform()
        return render(request,"stud.html",{"form":form})

    def post(self,request):
        form=studentform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form=studentform()
            return render(request,"stud.html",{"form":form}) 
        
        else:
            return render(request,"stud.html",{"form":form})
        
class studentlist(View):
    def get(self,request):
        qs=Student.objects.all()
        return render(request,"studlist.html",{"form":qs})
    

class getstud(View):
    def get(self,request,*args,**kwargs):
        # **kwargs - provides with flexibility to use keyword arguments in our program.
        # Using it as parameter.We can add more than one values by using kwargs.
        id=kwargs.get("one")
        qs=Student.objects.get(id=id)
        return render(request,"studentd.html",{"form":qs}) 


class studdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Student.objects.get(id=id).delete()
        return redirect('stud-l')
    


                   
        

        