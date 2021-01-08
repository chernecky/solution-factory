from django.urls import path
from solfactRest.poll.views import PollCreateView, QuestionDetailView, AnswerListView

app_name = 'poll'
urlpatterns = {
    path('poll/create/', PollCreateView.as_view()),
    path('all/Question/<int:pk>/', QuestionDetailView.as_view()),
    path('all/Answer', AnswerListView.as_view()),
}
