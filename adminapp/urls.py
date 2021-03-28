from django.urls import path
# from .views import GenerateBills,GenerateSalaries
from .views import Branches,BranchDetail,Newspapers,NewsPaperDetail
urlpatterns = [
    path('branches/',Branches.as_view()),
    path('branch/<int:pk>',BranchDetail.as_view()),
    path('newspapers/',Newspapers.as_view()),
    path('newspaper/<int:pk>',NewsPaperDetail.as_view())
]