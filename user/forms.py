from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.Form):
	email = forms.CharField(max_length=254)
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_ = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('email already taken')
		return email

	def clean_password_2(self):
		# Check if both passwords match
		password_1 = self.cleaned_data.get('password')
		password_2 = self.cleaned_data.get('CNFpassword')
		if password_1 and password_2 and password_1 != password_2:
			raise forms.ValidationError("Password don't Match")
		return password_2

class SetPasswordForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
	password_ = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


class UserAdminCreationForm(forms.ModelForm):
	"""
	A form for creating new users. Includes all the required fields,
	plus a repeated password.
	"""
	password = forms.CharField(label='password', widget=forms.PasswordInput)
	password_ = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('email',)

	def clean_password_2(self):
		# Check if both passwords match
		password_1 = self.cleaned_data.get('password')
		password_2 = self.cleaned_data.get('CNFpassword')
		if password_1 and password_2 and password_1 != password_2:
			raise forms.ValidationError("Password don't Match")
		return password_2

	def save(self, commit=True):
		# save the entered password in the hash format
		user = super(UserAdminCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password_1'])
		# user.active = false
		if commit:
			user.save()
		return user


class UserAdminChangeForm(forms.ModelForm):
	"""
	A form for updating users. Includes all the fields on
	the user, but replaces the password field with admin's
	password hash display field.
	"""
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('email', 'password', 'admin')

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the field
		# does not have access to the initial data.
		return self.initial['password']
