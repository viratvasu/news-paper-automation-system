from django.urls import path
from .views import Paperboys,PaperBoysModify,Generate,getInfo
urlpatterns = [
    path('paperboys/',Paperboys.as_view()),
    path('paperboy/<int:pk>',PaperBoysModify.as_view()),
    path('generate/',Generate.as_view()),
    path('info/',getInfo.as_view())
]