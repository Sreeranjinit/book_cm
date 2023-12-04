from django.db import models
#python manage.py makemigrations- ORM ne querry language lekk convert cheyyan.
# -----------------------------
#python manage.py migrate - querry language ne sqlite lekk convert(database lekk store cheyyan) cheyyan  
#  ----------------------                                                                         
# models: which is used to perform certain actions using data.eg - CRUD(create,read/retrieve,,update,delete)
# django default db - sqlite3
# python manage.py createsuperuser - database nu usernam eum passwor um kodukkan

class Employee(models.Model):
    email=models.EmailField(null=True)
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name
    

# class Student(models.Model):
#     name=models.CharField(max_length=20)
#     age=models.PositiveIntegerField()
#     email=models.EmailField(unique=True)
#     place=models.CharField(max_length=20)
#     gender=models.CharField(max_length=10)

#     def __str__(self):
#         return (self.name,self.place,self.gender)
    

    
class emp(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    contact=models.IntegerField()



#makemigrations
#migrate
class item(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    details=models.CharField(max_length=50)  

class book(models.Model):
    title=models.CharField(max_length=30)
    autor=models.CharField(max_length=20)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)


    def __str__(self):
        # return self.title 
        return f"{self.title} -{self.autor} -{self.publication_year} -{self.genre} " 


class mobilModel(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    details=models.CharField(max_length=30)


    def __str__(self):
        return self.name  


class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    course=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    place=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.age} {self.course} {self.gender} {self.place}"
        # return self.name
         