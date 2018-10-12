from django.urls import path
from app_one import views
app_name = 'app_one'
urlpatterns = [
    path('',views.List.as_view(),name='list'),
    path('<int:pk>/', views.Detail.as_view(), name='student_details'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path('create/',views.SchoolCreateView.as_view(),name='create')

]
