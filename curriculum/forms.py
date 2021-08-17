from django import forms
from .models import Lesson, Comment, Reply

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = (
                    "name", 
                    "position", 
                    "video", 
                    "ppt", 
                    "Notes")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        label = {"body": "Comment"}

        widgets = {
            'body':forms.Textarea(
                attrs = {'class':'form-controll', 'rows': 4, 'cols': 70, 'pleaceholder':"Izoh yozing"}
            )
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply-body':forms.Textarea(
                attrs = {'class':'form-controll', 'rows': 2, 'cols': 10, 'pleaceholder':"Javob yozing"}
            )
        }
