from django.urls import path
from .import views
urlpatterns = [
    path("add_money/", views.AddMoney, name="add_money"),
    path("report/", views.Cashout, name="transaction_report"),
    path("cashout/", views.Cashout, name="cashout"),
    path("send_money/", views.SendMoney, name="send_money"),
    path("loan/", views.Loan, name="loan"),
    path("transaction-history/", views.transaction_history, name="transaction_history"),
    path("pending_loans/", views.PendingLoans, name="pending_loans"),
    path("loan_pay/<int:loan_id>/", views.LoanPay, name="loan_pay"),
]