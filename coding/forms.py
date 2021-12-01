from django import forms
from django.forms.widgets import RadioSelect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(
			choices=choice_list, widget=RadioSelect(attrs={'class': 'mr-2 align-middle', 'type': 'radio'})
		)

class NewUser(UserCreationForm):
	username = forms.CharField(
		required=True,
		label='Username',
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'style': 'margin-bottom:20px'}),
	)
	email = forms.EmailField(
		required=True,
		label='Email Address',		
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@company.com', 'style': 'margin-bottom:20px'}),
	)

	password1 = forms.CharField(
		required=True,
		label='Password',
		help_text='<ul><li>Password can’t be too similar to personal information.</li><li>Password must contain at least 8 characters.</li><li>Password can’t be a commonly used password.</li><li>Password can’t be entirely numeric.</li></ul>',
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id':'exampleConfirmPassword7'}),
	)

	password2 = forms.CharField(
		required=True,
		label='Confirm Password',
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the same password again', 'id':'exampleConfirmPassword7' , 'style': 'margin-bottom:25px'}),
	)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUser, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user