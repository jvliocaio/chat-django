from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create-room', views.create_room, name="create-room"),
    path('<pk>', views.RoomDetailView.as_view(), name="room_detail"),
    path('<pk>/send', views.send_message, name="send_message"),
]
