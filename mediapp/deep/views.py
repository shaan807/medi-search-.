from django.shortcuts import render
import keras
from PIL import Image
import numpy as np
import os
from django.core.files.storage import FileSystemStorage
import h5py as h5

media = 'media'
model = keras.models.load_model('trained.h5')


def makepredictions(path):
    img = Image.open(path)

    img_d = img.resize((255, 255))

    if len(np.array(img_d).shape) < 4:
        rgb_img = Image.new("RGB", img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img = img_d

    rgb_img = np.array(rgb_img, dtype=np.float64)
    rgb_img = rgb_img.reshape(-1, 255, 255, 3)

    predictions = model.predict(rgb_img)
    result_names = ["glioma", "meningioma", "notumor", "pituitary"]
    prediction_index = int(np.argmax(predictions))

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


    
