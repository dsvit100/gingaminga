from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/update', views.update, name='update'),

    # Comment
    # Create
    path('<int:question_id>/comment/create', views.comment_create, name='comment_create'),
]