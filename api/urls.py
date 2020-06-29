from rest_framework import routers
from django.urls import path
from . import views
from .views import NoteList, NoteDetail

router = routers.DefaultRouter()

router.register('/note', NoteList)
router.register('note_details', NoteDetail)

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>', views.NoteDetail.as_view())
]