from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from polls import views

urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
