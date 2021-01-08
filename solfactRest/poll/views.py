from django.shortcuts import render
from rest_framework import generics
from poll.models import Poll
import poll.serializers
from solfactRest.poll.permission import IsOwnerOrreadOnly
from rest_framework.permissions import IsAuthenticated isAdminUser

class PollCreateView():
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated)