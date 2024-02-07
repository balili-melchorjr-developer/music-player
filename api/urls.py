from django.urls import path
from .views import RoomView, ProjectViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('project', ProjectViewset, basename='project')
urlpatterns = router.urls



# urlpatterns = [
#     path('room', RoomView.as_view())
# ]

