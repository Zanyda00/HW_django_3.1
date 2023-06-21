from django.urls import path

from .views import SensrListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView
urlpatterns = [
    path('sensors/', SensrListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementCreateAPIView.as_view()),

]
