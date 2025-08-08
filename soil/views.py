from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import joblib
import numpy as np
from .models import SoilData
from .forms import SoilDataForm

model = joblib.load("soil_model.pkl")

SOIL_RECOMMENDATIONS = {
    "Sandy Soil": "Add organic matter, use compost, and increase irrigation.",
    "Loamy Soil": "Maintain nutrients with crop rotation and compost.",
    "Clayey Soil": "Improve drainage, add gypsum, and use raised beds.",
    "Silty Soil": "Improve drainage, avoid over-watering, and maintain aeration.",
    "Desert Soil": "Increase organic matter, use mulch, and enhance water retention.",
    "Peaty Soil": "Improve drainage, use lime to reduce acidity, and mix with sand.",
    "Chalky Soil": "Add organic matter, use sulfur to lower pH, and apply fertilizers.",
}

def login_view(request):
    if request.user.is_authenticated:
        return redirect('soil_quality')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('soil_quality')
        else:
            return render(request, 'soil/login.html', {'error': 'Invalid credentials'})
    return render(request, 'soil/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def soil_quality_view(request):
    if request.method == 'POST':
        form = SoilDataForm(request.POST)
        if form.is_valid():
            soil_entry = form.save(commit=False)
            features = np.array([[soil_entry.ph, soil_entry.nitrogen, soil_entry.phosphorus, 
                                  soil_entry.potassium, soil_entry.organic_carbon, 
                                  soil_entry.sand, soil_entry.silt, soil_entry.clay]])
            predicted_soil = model.predict(features)[0]
            soil_entry.soil_type = predicted_soil
            soil_entry.save()
            return redirect('soil_result', soil_id=soil_entry.id)
    else:
        form = SoilDataForm()
    return render(request, 'soil/soil_quality.html', {'form': form})

@login_required
def soil_result_view(request, soil_id):
    soil_entry = get_object_or_404(SoilData, id=soil_id)
    return render(request, 'soil/result.html', {
        'prediction': soil_entry.soil_type,
        'recommendation': SOIL_RECOMMENDATIONS.get(soil_entry.soil_type, "No recommendations available."),
    })

@login_required
def about_view(request):
    return render(request, 'soil/about.html')

@login_required
def contact_view(request):
    return render(request, 'soil/contact.html')

@login_required
def soil_view(request):
    return render(request, 'soil/soil.html')

from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('soil_quality')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'soil/signup.html', {'form': form})
