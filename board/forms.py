from django.forms import forms

from board.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)