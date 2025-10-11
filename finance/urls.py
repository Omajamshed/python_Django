from django.urls import path
# from finance.views import home,homeview
from finance.views import RegisterView,DashboardView,TransactionCreateView,TransactionListView,GoalCreateView
urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('',DashboardView.as_view(),name="dashboard"),
    path('transaction/add/',TransactionCreateView.as_view(),
         name="transaction_add"),
    path('transactions/',TransactionListView.as_view(),name="transaction_list"),
    path('goal/add/',GoalCreateView.as_view(), name="goal_add"),

]

