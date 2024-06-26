from django.urls import path
from . import views
# from .views import user_login

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('', views.user_login, name='login'),
     path("add/", views.details, name="add_patient"),
    path("patient/<str:Name>/", views.display, name="view_patient"),
    path('all/', views.view_all_patients, name='view_all_patients'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('base/', views.base, name='base'),
]
