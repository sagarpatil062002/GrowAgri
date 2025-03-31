from django.shortcuts import render
import pickle
import numpy as np

# Load the Random Forest model
with open('./savedModels/rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

def home(request):
    return render(request, 'home.html')

def predict_form(request):
    return render(request, 'main.html')

def formInfo(request):
    nitrogen = request.GET.get('Nitrogen')
    phosphorus = request.GET.get('Phosphorus')
    potassium = request.GET.get('Potassium')
    temperature = request.GET.get('temperature')
    humidity = request.GET.get('humidity') 
    pH_value = request.GET.get('pH_value')
    rainfall = request.GET.get('rainfall')

    # Prepare the input data for prediction
    new_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, pH_value, rainfall]], dtype=float)

    # Predict the crop
    predicted_crop = rf_model.predict(new_data)

    # Remove square brackets and single quotes from the predicted crop
    predicted_crop = predicted_crop[0]

    print("Predicted Crop:", predicted_crop)

    return render(request, 'result.html', {'result': predicted_crop})
