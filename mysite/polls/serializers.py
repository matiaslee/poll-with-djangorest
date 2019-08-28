import datetime as dt
from rest_framework import serializers
from polls.models import Question, Choice

class QuestionSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField()
    pub_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        validated_data['pub_date'] = dt.datetime.now()
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Poll` instance, given the validated data.
        """
        instance.question_text = validated_data.get('question_text', instance.question_text)

class QuestionSerializerWithMS(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Question
        fields = ['pk', 'question_text', 'pub_date']

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        validated_data['pub_date'] = dt.datetime.now()
        return Question.objects.create(**validated_data)
