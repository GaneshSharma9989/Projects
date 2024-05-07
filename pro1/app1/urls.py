# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.details, name="add_patient"),
    path("patient/<str:Name>/", views.display, name="view_patient"),
    path('all/', views.view_all_patients, name='view_all_patients'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('base/', views.base, name='base'),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),


    # Add other paths as needed
]
