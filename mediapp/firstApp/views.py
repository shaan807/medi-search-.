from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import joblib
import json, os
import numpy as np
import pandas as pd
from .models import snh
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# Create your views here.

def index(request):
    return render(request, "index.html")



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same !")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')

        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect !!!")
        
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



from django.shortcuts import render
from django.http import HttpResponse
from .models import snh  
import joblib

# def result(request):
#     model = joblib.load('../model_joblib_heart')
def result(request):
    model = joblib.load('../model_joblib_heart')
    # if 'user' in request.session:
    #     model = joblib.load('../model_joblib_heart')
    #     data = model.values
    #     X = data[:, :-1]
    #     Y = data[:, -1:]

    #     value = ''

    #     if request.method == 'POST':
    #         features = [
    #             'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    #             'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    #         ]

    #         user_data = np.array([
    #             float(request.POST[feature]) for feature in features
    #         ]).reshape(1, -1)

    #         rf = RandomForestClassifier(
    #             n_estimators=16,
    #             criterion='entropy',
    #             max_depth=9
    #         )

    #         rf.fit(np.nan_to_num(X), Y)
    #         predictions = rf.predict(user_data)

    #         if int(predictions[0]) == 1:
    #             value = 'have'
    #         elif int(predictions[0]) == 0:
    #             value = "don\'t have"
   

    sex_input = request.GET['sex'].lower()
    if sex_input == 'male':
        sex_value = 1
    elif sex_input == 'female':
        sex_value = 0
    else:
         return HttpResponse("Invalid input for 'sex'. Please enter 'male' or 'female'.")


    list = []
    list.append(float(request.GET['age']))
    list.append(float(sex_value))
    list.append(float(request.GET['cp']))  # Change here for CP
    list.append(float(request.GET['trestbps']))
    list.append(float(request.GET['chol']))
    list.append(float(request.GET['fbs']))
    list.append(float(request.GET['restecg']))
    list.append(float(request.GET['thalach']))
    list.append(float(request.GET['exang']))
    list.append(float(request.GET['oldpeak']))
    list.append(float(request.GET['slope']))
    list.append(float(request.GET['ca']))
    list.append(float(request.GET['thal']))
    # list.append(float(request.GET['target']))  # Add target here

    answer = model.predict([list]).tolist()[0]

    # b = snh(
    #     age=request.GET['age'],
    #     sex=sex_value,
    #     cp=request.GET['cp'],
    #     trestbps=request.GET['trestbps'],
    #     chol=request.GET['chol'],
    #     fbs=request.GET['fbs'],
    #     restecg=request.GET['restecg'],
    #     thalach=request.GET['thalach'],
    #     exang=request.GET['exang'],
    #     oldpeak=request.GET['oldpeak'],
    #     slope=request.GET['slope'],
    #     ca=request.GET['ca'],
    #     thal=request.GET['thal'],
    #     target=request.GET['target']
    # )
    # b.save()
    if answer == 0 :
        answer = 'You seem to be healthy and might not have heart disease.'
    else:
        answer = 'You may have heart disease.'

    return render(request, "index2.html", {'answer':answer})