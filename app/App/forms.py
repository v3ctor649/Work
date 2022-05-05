from django import forms

class QuizForm(forms.Form):
    count = forms.IntegerField()