from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginViews
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-creator/', TaskCreate.as_view(), name='task-creator'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-deleter/<int:pk>/', DeleteView.as_view(), name='task-deleter')
]
