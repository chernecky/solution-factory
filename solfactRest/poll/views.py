from rest_framework import generics
from solfactRest.poll.models import Poll
import solfactRest.poll.serializers
from solfactRest.poll.permission import IsOwnerOrreadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from solfactRest.poll.serializers import PollDetailSerializer, QuestionDetailSerializer


class PollCreateView(generics.CreateAPIView):
    serializer_class = PollDetailSerializer
    permission_classes = (IsOwnerOrreadOnly, IsAuthenticated)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Poll.object.all()
    permission_classes = (IsOwnerOrreadOnly, IsAuthenticated)


class AnswerListView(generics.ListAPIView):
    serializer_class = solfactRest.AnswerListSerializer
    permission_classes = IsAdminUser
