from rest_framework import serializers
from solfactRest.poll.models import Poll, Answer

from solfactRest.poll.models import Question


class PollDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = 'title'


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = 'answer'
