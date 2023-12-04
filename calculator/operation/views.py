from django.shortcuts import render
from  django.views.generic import View
from operation.forms import Formname,NewForm,EmiForm,Signup,Signin

class FormView(View):
    def get(self,request):
        form=Formname()  #formname nnuulla class ne variable kk assign cheythu vechuuu
        return render(request,"form.html",{"form":form})
    def post(self,request):
        print(request.POST)
        form=Formname(request.POST)
        if form.is_valid():
            print("myname",form.cleaned_data["name"])
            print("email",form.cleaned_data["email"])
            print("address",form.cleaned_data["address"])
            print("password",form.cleaned_data["password"])
            print("phone number :",form.cleaned_data["phone"])
            form=Formname()   #submit cheyth kaynjal form blank ayi nilkkan vendiyanu ingane kodukkunnath
        else:
            print("good bye")

        return render(request,"form.html",{"form":form})
    

class newView(View):
    def get(self,request):
        formm=NewForm
        return render(request,"f.html",{"formm":formm}) 
    def post(self,request):
        print(request.POST)
        formm=NewForm(request.POST) 
        if formm.is_valid(): 
            print("name :",formm.cleaned_data["name"])
            print("email :",formm.cleaned_data["email"])
            formm=NewForm()
        else:
            print("quit")
        return render(request,"f.html",{"formm":formm})

class EmiView(View):
    def get(self,request):
        form=EmiForm()
        return render(request,"emi.html",{"form":form})
    def post(self,request):
        print(request.POST)
        form=EmiForm(request.POST)
        if form.is_valid():
            # print("loan amount :",form.cleaned_data["loan_amount"])
            # print("Tenure :",form.cleaned_data["tenure"])
            # print("interest :",form.cleaned_data["interest"])
                             #OR
            print(form.cleaned_data)
            loan_amount=form.cleaned_data.get('loan_amount')
            tenure=form.cleaned_data.get('tenure')
            interest=form.cleaned_data.get('interest')
            n=tenure*12
            # E=p*r*(1+r)^n/((1+r)^n-1)
            r=interest
            p=loan_amount
            emi=p*r*(1+r)**n/((1+r)**n-1)
            print(emi)
            form=EmiForm()
        else:
            print("leave it")
        return render(request,"emi.html",{"form":form}) 

class signupView(View):
    def get(self,request):
        form=Signup()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        form=Signup(request.POST)
        if form.is_valid():
            print("name :",form.cleaned_data["name"])
            print("email :",form.cleaned_data["email"])
            print("password :",form.cleaned_data["password"])
            form=Signup()
        else:
            print("leave it")
        return render(request,"signup.html",{"form":form})  

class signinview(View):
    def get(self,request):
        form=Signin()
        return render(request,"signin.html",{"form":form}) 
    def post(self,request):
        form=Signin(request.POST)
#check whether the password correct or incorrect
        if form.is_valid():
            name =form.cleaned_data.get("name")
            email =form.cleaned_data.get("email")
            password1 =form.cleaned_data.get("password")
            password2=form.cleaned_data.get("confirm_password")            
            if password1==password2:
                print(form.cleaned_data)
                print("match")
            else:
                print(form.cleaned_data)
                print("password not match!!!!")    
        else:
            print("leave it")
            form=Signin()
        return render(request,"signin.html",{"form":form})  

                      #OR
                         
class signinview(View):
    def get(self,request):
        form=Signin()
        return render(request,"signin.html",{"form":form}) 
    def post(self,request):
        form=Signin(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password')==form.cleaned_data.get('confirm_password'):
                print(form.cleaned_data)
                form=Signin()
            else:
                print(form.cleaned_data)
                print("password not match!!!!")    
        else:
            print("leave it")
            form=Signin()
        return render(request,"signin.html",{"form":form})  
     


# Create your views here.

class HelloWorldView(View):
    def get(self,request):
        return render(request,"Helloworld.html")
    
class HelloView(View):
    def get(self,request):
        return render(request,"hello.html")

class goodview(View):
    def get(self,request):
        return render(request,"good.html")

class AddView(View):
    def get(self,request):    #sever lekk request kodukkunnu.sever oru html pagr return cheyyunnu
        return render(request,"add.html") 
    def post(self,request):
        print(request.POST)   #send cheytha data yude operation perform cheyth response return cheyyunnu
        request.POST.get("num1")  #django il data ye keyvalue pair(dictionay)ayittanu store cheyyunnath. num1 key ne get cheyth edukkn
        request.POST.get("num2") 
        n1=int(request.POST["num1"])  #num1 key ne get cheythaanu value edukkunnath 
        n2=int(request.POST["num2"])  
        result=n1+n2 
        print(result)
        return render(request,"add.html",{"result":result})    
     

class subsractview(View):
    def get(self,request):
        return render(request,"sub.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("num1")
        request.POST.get("num2") 
        n1=int(request.POST["num1"])  
        n2=int(request.POST["num2"])  
        result=n1-n2 
        print(result)
        return render(request,"sub.html",{"result":result})  

class MulView(View):
    def get(self,request):
        return render(request,"mul.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("num1","num2")
        n1=int(request.POST["num1"])
        n2=int(request.POST["num2"])
        result=n1*n2
        print(result)
        return render(request,"mul.html",{"result":result}) 

class  DivView(View):
    def get(self,request):
        return render(request,"div.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("first num","second num")
        n1=int(request.POST["first num"])
        n2=int(request.POST["second num"])
        result=n1/n2
        print(result)
        return render(request,"div.html",{"result":result})

class leapyearview(View):
    def get(self,request):
        return render(request,"leap.html")
    def post(self,request):
        request.POST.get("year")
        year=int(request.POST.get("year"))  #year nnulla keyde value retrieve cheyth edukkananu request.POST.get
        if year%100==0 and year%400==0:
            res="leap year"
        elif year%4==0 and year%100!=0:
           res= "leap year"
        else:
            res="not leap year"
        return render(request,"leap.html",{"result":res})          
        
class NumberView(View):
    def get(self,request):
        return render(request,"num.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST.get("number"))
        if num%2==0:
            res="even"
        else:
            res="odd"

        return render(request,"num.html",{"res":res})


class large(View):
    def get(self,request):
        return render(request,"large.html")
    def post(self,request):
        request.POST.get("num1")
        request.POST.get("num2")
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        if num1>num2:
            res= (num1, "is larger")
        else:
            res= (num2, "is larger") 
        return render(request,"large.html",{"res":res})  

class armstsrong(View):
    def get(self,request):
        return render(request,"armstrong.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST.get("number"))
        sum=0
        temp=num
        while(num>0):
            dig=num%10
            sum+=dig**3
            num=num//10
        if temp==sum:
            res="armstrong number"
        else:
            res="not armstrong"    

        return render(request,"armstrong.html",{"res":res}) 
            
class paliandrome(View):
    def get(self,request):
        return render(request,"paliandrome.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST.get("num"))
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num//=10
        if temp==rev:
            result="paliandome"
        else:
            result="not paliandrome"
        return render(request,"paliandrome.html",{"res":result})

class String(View):
    def get(self,request):
        return render(request,"str.html")
    def post(self,request):
        request.POST.get("str")
        strg=request.POST.get("str") 
        s=strg[::-1]
        if s==strg:
            res="paliandrome"
        else:
            res="not paliandrome"
        return render(request,"str.html",{"res":res})
    
class Cirly(View):
    def get(self,request):
        return render(request,"dict.html")
    def post(self,request):
        request.POST.get("barcket") 
        str=request.POST.get("bracket")
        s="{()}"
        if s==str:
            res="valid"
        else:
            res="invalid"
        return render(request,"dict.html",{"res":res})    
            
class greeting(View):
    def get(self,request):
        return render(request,"greet.html")
    def post(self,request):
        request.POST.get("greet")
        str=request.POST.get("greet")
        res=f"Hello {str} welcome to luminar"
        return render(request,"greet.html",{"res":res})
    
class prime(View):
    def get(self,request):
        return render(request,"prime.html")
    def post(self,request):
        request.POST.get("num")
        number=int(request.POST.get("num"))
        if number==1:
            res=" 1 is not a prime number" 
        elif number==2:
            res="2 is prime number"
        else:        
            for i in range(2,number):
                if number%i==0:
                    res="not prime"
                    break
                else:
                    res="prime"
        return render(request,"prime.html",{"res":res}) 


class fibonacci(View):
    def get(self,request):
        return render(request,"fib.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST["num"])
        n1=0
        n2=1
        count=0
        res=""
        if num<=0:
            res="The fibannoci series is"
        elif num==1: 
            res=f"{n1}"
        else:
            while count<num:
                res+=f"{n1} "
                n3=n1+n2
                n1=n2
                n2=n3
                count+=1
        return render(request,"fib.html",{"res":res})