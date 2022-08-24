from django.urls import path,include
from AdvanceCBV_App import views


app_name = 'AdvanceCBV_App'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),



    path('<int:pk>/',views.SchoolDetaiView.as_view(),name='detail'),



    path('create/',views.SchoolCreateView.as_view(),name='create'),


    path('Update/(<int:pk>/)',views.SchoolUpdateView.as_view(),name='update'),



    path('delete/(<int:pk>/)',views.SchoolDeleteView.as_view(),name='delete'),

]
