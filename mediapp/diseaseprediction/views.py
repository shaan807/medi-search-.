from django.shortcuts import render,HttpResponse
import joblib
import json,os
import numpy as np
import pandas as pd
import psycopg2
# from .models import 
from firstApp import views
from firstApp.models import snh


# Create your views here.
def index1(request):
    return render(request, 'index1.html', {})

def result(request):
    model = joblib.load('../models/model.joblib')
    list = []
    list.append(float(request.GET['itching']))
    list.append(float(request.GET['skin_rash']))
    list.append(float(request.GET['joint_pain']))
    list.append(float(request.GET['stomach_pain']))
    list.append(float(request.GET['vomiting']))
    list.append(float(request.GET['fatigue']))
    list.append(float(request.GET['cough']))
    list.append(float(request.GET['high_fever']))
    list.append(float(request.GET['breathlessness']))
    list.append(float(request.GET['headache']))
    list.append(float(request.GET['nausea']))
    list.append(float(request.GET['abdominal_pain']))
    
    
    
    input_symptoms = ['obesity', 'weight_gain', 'fluid_overload.1', 'weakness_of_one_body_side', 'stiff_neck', 'continuous_sneezing', 'patches_in_throat', 'palpitations', 'hip_joint_pain', 'shivering', 'blood_in_sputum', 'yellowing_of_eyes', 'constipation', 'runny_nose', 'swelling_of_stomach', 'brittle_nails', 'inflammatory_nails', 'cold_hands_and_feets', 'fast_heart_rate', 'receiving_unsterile_injections', 'blister', 'bloody_stool', 'swollen_extremeties', 'extra_marital_contacts', 'family_history', 'skin_peeling', 'lack_of_concentration', 'dischromic__patches', 'knee_pain', 'painful_walking', 'weakness_in_limbs', 'excessive_hunger', 'sinus_pressure', 'unsteadiness', 'continuous_feel_of_urine', 'red_sore_around_nose', 'indigestion', 'blurred_and_distorted_vision', 'back_pain', 'loss_of_appetite', 'fluid_overload', 'silver_like_dusting', 'altered_sensorium', 'anxiety', 'mood_swings', 'pain_in_anal_region', 'muscle_pain', 'irregular_sugar_level', 'prominent_veins_on_calf', 'belly_pain', 'bladder_discomfort', 'abnormal_menstruation', 'sunken_eyes', 'receiving_blood_transfusion', 'dehydration', 'redness_of_eyes', 'pain_during_bowel_movements', 'chills', 'blackheads', 'internal_itching', 'burning_micturition', 'acute_liver_failure', 'small_dents_in_nails', 'yellow_urine', 'history_of_alcohol_consumption', 'depression', 'drying_and_tingling_lips', 'swollen_legs', 'nodal_skin_eruptions', 'diarrhoea', 'muscle_weakness', 'polyuria', 'coma', 'movement_stiffness', 'puffy_face_and_eyes', 'ulcers_on_tongue', 'irritability', 'dark_urine', 'visual_disturbances', 'yellowish_skin', 'congestion', 'mucoid_sputum', 'throat_irritation', 'loss_of_balance', 'stomach_bleeding', 'swelled_lymph_nodes', 'malaise', 'mild_fever', 'phlegm', 'neck_pain', 'scurring', 'pain_behind_the_eyes', 'loss_of_smell', 'acidity', 'chest_pain', 'spotting__urination', 'toxic_look_(typhos)', 'slurred_speech', 'distention_of_abdomen', 'cramps', 'enlarged_thyroid', 'watering_from_eyes', 'weight_loss', 'dizziness', 'swelling_joints', 'pus_filled_pimples', 'red_spots_over_body', 'sweating', 'lethargy', 'spinning_movements', 'increased_appetite', 'bruising', 'rusty_sputum', 'yellow_crust_ooze', 'swollen_blood_vessels', 'muscle_wasting', 'foul_smell_of_urine', 'restlessness', 'passage_of_gases', 'irritation_in_anus']
    
    
    for symptom in input_symptoms:
        list.append(float(request.GET.get(symptom, 0)))
    
    answer = int(model.predict([list]).tolist()[0])
        
    dict = {0: 'Fungal_infection', 1: 'Allergy', 2: 'GERD', 3: 'Chronic_cholestasis', 4: 'Drug_Reaction', 5: 'Peptic_ulcer_diseae', 6: 'AIDS', 7: 'Diabetes_', 8: 'Gastroenteritis', 9: 'Bronchial_Asthma', 10: 'Hypertension_', 11: 'Migraine', 12: 'Cervical_spondylosis', 13: 'Paralysis_(brain_hemorrhage)', 14: 'Jaundice', 15: 'Malaria', 16: 'Chicken_pox', 17: 'Dengue', 18: 'Typhoid', 19: 'hepatitis_A', 20: 'No Disease . You are Safe', 21: 'Hepatitis_C', 22: 'Hepatitis_D', 23: 'Hepatitis_E', 24: 'Alcoholic_hepatitis', 25: 'Tuberculosis', 26: 'Common_Cold', 27: 'Pneumonia', 28: 'Dimorphic_hemmorhoids(piles)', 29: 'Heart_attack', 30: 'Varicose_veins', 31: 'Hypothyroidism', 32: 'Hyperthyroidism', 33: 'Hypoglycemia', 34: 'Osteoarthristis', 35: 'Arthritis', 36: '(vertigo)_Paroymsal__Positional_Vertigo', 37: 'Acne', 38: 'Urinary_tract_infection', 39: 'Psoriasis', 40: 'Impetigo'}
    answer = dict[answer]
    return render(request, 'index1.html', {'answer':answer})


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def index2(request):
    return render(request,'index2.html')

def result2(request):
    model = joblib.load('../models/model_joblib_heart.joblib')
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

def department(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    return render(request,'contact.html')

def index_deep(request):
    return render(request,"index_deep.html")

###########deep###########

from django.shortcuts import render
import keras
from PIL import Image
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
import h5py as h5

media = 'media'
model = '../models/trained.h5'


def makepredictions(path):
    img = Image.open(path)

    img_d = img.resize((255, 255))

    if len(np.array(img_d).shape) < 4:
        rgb_img = Image.new("RGB", img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img = img_d
# Assuming the image is 255x255 pixels with 3 color channels (RGB)
    rgb_img = np.array(rgb_img, dtype=np.float64)
    rgb_img = rgb_img.reshape(1, 255, 255, 3)  # Reshape for prediction

    predictions = model.predict(rgb_img)
    result_names = ["glioma", "meningioma", "notumor", "pituitary"]
    prediction_index = int(np.argmax(predictions))
    predicted_label = result_names[prediction_index]


    result_folder_name = result_names[prediction_index]

    # Save the image to a folder based on the predicted result
    media_root = 'media'
    folder_path = os.path.join(media_root, result_folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    image_name = os.path.basename(path)
    new_image_path = os.path.join(folder_path, image_name)
    
    img.save(new_image_path)  # Save the image to the respective folder

    
    delete_images(media_root)
    
    
    if prediction_index == 0:
        result = "Result: glioma"
    elif prediction_index == 1:
        result = "Result : meningioma"
    elif prediction_index == 2:
        result = "Result is : notumor"
    else:
        result = "Result : pituitary"

    return result,new_image_path

def delete_images(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            os.remove(file_path)
            print(f"Deleted: {filename}")
            
            
            
def index_deep(request):
    if request.method == "POST" and request.FILES['upload']:
        if 'upload' not in request.FILES:
            err = 'No Images Selected'
            return render(request, 'index_deep.html',{'err': err})
        f = request.FILES['upload']
        if f == '':
            err = 'No Files Selected'
            return render(request, 'index_deep.html', {'err': err})
        
        upload =request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name,upload)
        file_url = fss.url(file)
        predictions,new_image_path = makepredictions(os.path.join(media, file))
        

        return render(request, 'index_deep.html', {'pred': predictions, 'file_url': new_image_path})
    else:
        return render(request, 'index_deep.html')


    
