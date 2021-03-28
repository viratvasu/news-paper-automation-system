from django.urls import path
from .views import (
    SubscriptionView,
    BillInfo,PayBill,
    PaymentDetails,
    ChangePassword,
    ChangeUserName,
    RemoveFromSubscription,
    GetPapers,
    DailyReportView,
    getInfo
)
urlpatterns = [
    path('subscription/',SubscriptionView.as_view()),
    path('subscription/delete/<int:pk>',RemoveFromSubscription.as_view()),
    path('bills/',BillInfo.as_view()),
    path('pay-bill/<int:pk>',PayBill.as_view()),
    path('payment-details/',PaymentDetails.as_view()),
    path('change-username/',ChangeUserName.as_view()),
    path('change-password/',ChangePassword.as_view()),
    path('papers/',GetPapers.as_view()),
    path('reports/',DailyReportView.as_view()),
    path('info/',getInfo.as_view()),
]