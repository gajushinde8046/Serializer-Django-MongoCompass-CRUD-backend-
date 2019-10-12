# Serializer-Django-MongoCompass-CRUD-backend-


first of clone or download the repository

1.Go to download location or wherever your repo located in my case and in first case dont go to serial folder
  
  C:\Users\HP\Downloads\Serializer-Django-MongoCompass-CRUD-backend--master\Serializer-Django-MongoCompass-CRUD-backend--master\
  
2.now open cmd in location bar (C:\Users\HP\Downloads\Serializer-Django-MongoCompass-CRUD-backend--master\Serializer-Django-MongoCompass-CRUD-backend--master\)
in your case location differs

3.now in command prompt set environment variable

  >>python -m venv env
  
4. now activate the env
  
  >>env\Scripts\activate
  
5.now install django
  
   >>pip install django
   
6. install django rest framework
  
  >>pip install djangorestframework
  

7.install django as i use MongoDB as DB 
  
  >>pip install djongo

8.now connect Django with MongoDB

go to settings.py
  and set database as
  
  DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'serialProductDB',
    }
}
   that i have already set
 you dont need to set
 
9. now go to any IDE like pycharm or VS code


open serial folder from same the project
 you found two sub folders as serial and product
 
 now change directory to serial
>>...Serializer-Django-MongoCompass-CRUD-backend--master\Serializer-Django-MongoCompass-CRUD-backend--master\serial 

and
in serial folder
10.make migration
  
  serial>>python manage.py makemigrations

11. migrate the manage.py file
  
  serial>>python manage.py migrate

12.run server 
  
   serial>>python manage.py runserver
   
13.now open Mongo Compass is a UI form of DB
14. In that you get serialProductDB database 
in that product_product collection

to check api use Postman

15. For POST use 
    
    {
        "price":499,
        "productName":"Earphone",
        "description":"This is wireless earphone with mic"
    }
    
    use localhost:8000/product/get/ and POST method
  
 16. same for GET all listed items
  
  localhost:8000/product/get/
  
17. for PUT GET DELETE by name use
  
  localhost:8000/product/details/Earphone/
  
  PUT
       {
        "price":699,
        "productName":"Earphone",
        "description":"This is wireless earphone with mic"
    }
    
    It will update the value
    
 18. Same for GET and DELETE by name
  
  
    

 
