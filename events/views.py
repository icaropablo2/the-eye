from rest_framework import viewsets
from rest_framework import permissions

from events.serializers import EventSerializer
from events.models import Event


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]