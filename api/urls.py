from django.urls import path
from .views import RoomView, ProjectViewset, ProjectManagerViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('project', ProjectViewset, basename='project')
router.register('project-manager', ProjectManagerViewset, basename='project-manager')
urlpatterns = router.urls



# urlpatterns = [
#     path('room', RoomView.as_view())
# ]

