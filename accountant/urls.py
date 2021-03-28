from django.urls import path
from .views import GenerateBills,GenerateSalaries
urlpatterns = [
    path('generatebills/',GenerateBills.as_view()),
    path('generatesalaries/',GenerateSalaries.as_view()),
]