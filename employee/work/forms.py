from django import forms
from work.models import book,item,mobilModel,Student

class Empform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.IntegerField()

# class bookform(forms.Form):
    # title=forms.CharField()
    # autor=forms.CharField()
    # publication_year=forms.IntegerField()
    # genre=forms.CharField() 

             #OR

class bookform(forms.ModelForm):
    class Meta:
        model=book 
        fields='__all__'
        
        #or

        # fields=['title','autor','publication_year','genre']           
              
class itemform(forms.ModelForm):
    class Meta:
        model=item
        fields='__all__'

class mobileform(forms.ModelForm):
    class Meta:
        model=mobilModel
        fields='__all__'


class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

