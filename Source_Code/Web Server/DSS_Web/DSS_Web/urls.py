from django.urls import path, include

urlpatterns = [
    path('', include("Predict_Accident.urls")),
]
