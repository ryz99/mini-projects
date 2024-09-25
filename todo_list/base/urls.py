from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-creator/', TaskCreate.as_view(), name='task-creator'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update')
]
