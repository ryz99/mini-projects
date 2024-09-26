from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-creator/', TaskCreate.as_view(), name='task-creator'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-deleter/<int:pk>/', DeleteView.as_view(), name='task-deleter')
]
