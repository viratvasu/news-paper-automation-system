from django.urls import path
from .views import getSalaries,getUsersPapers,getInfo
urlpatterns = [
    path('salaries/',getSalaries.as_view()),
    path('work/',getUsersPapers.as_view()),
    path('info/',getInfo.as_view()),
]