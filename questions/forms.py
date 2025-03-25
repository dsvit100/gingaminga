from django.forms import ModelForm
from .models import Question, Comment

class QuestionForm(ModelForm):
    class Meta():
        model = Question
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        exclude = ('article', )