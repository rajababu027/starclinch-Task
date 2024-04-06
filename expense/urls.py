from django.urls import path
from expense import views

urlpatterns = [
    # path('', views.create_expense, name='index'),
    # path('split', views.create_split_expense, name='index'),
    path('', views.add_expense, name='add_expense'),
    path('all_users/', views.all_users_balances, name='all_users'),
    path('show_balances/<str:user_id>/', views.show_balances, name='show_balances'),
]