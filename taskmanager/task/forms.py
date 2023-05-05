from django import forms
from .models import Task

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('category','name','description','priority','deadline')
        widgets = {
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'priority':forms.Select(choices=Task.PRIORITY_CHOICES,attrs={
                'class':INPUT_CLASSES
            }),
            'deadline':forms.DateInput(attrs={
                'class':'form-control w-full py-4 px-6 rounded-xl border',
                'type':'date'
            })
        }

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name','description','is_done','priority','deadline')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'priority':forms.Select(choices=Task.PRIORITY_CHOICES,attrs={
                'class':INPUT_CLASSES
            }),
            'deadline':forms.DateInput(attrs={
                'class':'form-control w-full py-4 px-6 rounded-xl border',
                'type':'date'
            })
        }