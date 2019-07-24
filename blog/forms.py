from django import forms

from .models import Blog, Mentee, Mentor

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('judul', 'isi', 'pic')

class MenteeForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ('nama', 'quotes', 'pic')

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('nama', 'experience', 'julukan', 'quotes', 'pic')