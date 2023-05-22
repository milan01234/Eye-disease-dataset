from django.shortcuts import redirect,render
from django.http import HttpResponse
from myapp.models import Patient
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.core.files.storage import default_storage
import os

# Create your views here.
def home(request):
    return render(request,"authintication/index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lanem=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname 
        myuser.last_name=lanem
        myuser.save()
        messages.success(request,"Your  Account has been is Created successfully.")
        return render(request,"authintication/signin.html")

        
    return render(request,"authintication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,"index.html")
        else:
            messages.error(request,"Bad Credential")
            return render(request,"authintication/index.html")
    return render(request,"authintication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out successsfully")
    return render(request,"authintication/index.html")
def index(request):
    if request.method == 'POST': 
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        eye_image= request.FILES['upload']
        #file.save('temp.jpg')
        file_name=default_storage.save(eye_image.name,eye_image)
        file_url=default_storage.path(file_name)
        print(file_url) 
        # Load the trained model
        model = load_model("M:\Eye Disease Prediction\mysite\EyeDisease\myapp\model.h5")
        # Load the image and preprocess it
        img = image.load_img(file_url, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        #img_array = preprocess_input(img_array)
        # Make a prediction
        prediction = model.predict(img_array)
        #class lables
        class_labels = ['Cataract', 'Diabetic_retinopathy', 'Glucoma', 'Normal']
        #class_labels = ['Fracture','Non_fracture']
        # Convert the prediction to a category
        predicted_category = np.argmax(prediction)
        predicted_class = class_labels[predicted_category]
        # print(predicted_class)
        en=Patient(Patient_Name=name,Xender=gender,Age=age,Eye_Image=eye_image,Disease=predicted_class)
        en.save()
        return render(request,"index.html",{"readImg":'1',"user_image":file_url,"Prediction":predicted_class})
    return render(request,"index.html")

