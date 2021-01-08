from django.shortcuts import render
from rest_framework import generics
from solfactRest.poll.models import Poll
import solfactRest.poll.serializers
from solfactRest.poll.permission import IsOwnerOrreadOnly
from rest_framework.permissions import IsAuthenticated
from solfactRest.poll.serializers import AnswerDetailSerializer, QuestionDetailSerializer, PollDetailSerializer
isAdminUser

class PollCreateView():
    serializer_class = PollDetailSerializer
    permission_classes = (IsAuthenticated)


class PollCreateView():
    serializer_class = QuestionDetailSerializer
    permission_classes = (IsAuthenticated)

class PollCreateView():
    serializer_class = AnswerDetailSerializer
    permission_classes = (IsAuthenticated)