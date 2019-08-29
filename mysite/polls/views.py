from rest_framework import generics

from polls.models import Question
from polls.serializers import QuestionSerializerWithMS as QuestionSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    