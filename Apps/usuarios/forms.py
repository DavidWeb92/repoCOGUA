#creado manualmente
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from Apps.usuarios.models import Usuario

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['class'] = 'form-control'
		self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

#formulario de regitro en la base de datos
class RegistrarUsuarioForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder='Ingrese su contraseña'",
				'placeholder': 'Ingrese su contraseña',
				'id': 'password1',
				'required': 'required',
			}
		))

	password2 = forms.CharField(label = 'Contraseña de confirmacion',widget=forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder='Ingrese nuevamente su contraseña'",
				'placeholder': 'Ingrese nuevamente su contraseña',
				'id': 'password2',
				'required': 'required',
			}
		))

	class Meta:
		model = Usuario
		fields = ['nombres','apellidos','email','imagen']
		widgets = {
			'email': forms.EmailInput(
					attrs = {
						'class': 'form-control',
						'onfocus': "this.placeholder = ''",
						'onblur': "this.placeholder='Correo Electrónico'",
						'placeholder': 'Correo Electrónico',
					}
				),
			'nombres': forms.TextInput(
					attrs = {
						'class': 'form-control',
						'autocomplete': "off",
						'onfocus': "this.placeholder = ''",
						'onblur': "this.placeholder='Ingrese sus nombres'",
						'placeholder': 'Ingrese sus nombres',
					}
				),
			'apellidos': forms.TextInput(
					attrs = {
						'class': 'form-control',
						'autocomplete': "off",
						'onfocus': "this.placeholder = ''",
						'onblur': "this.placeholder='Ingrese sus apellidos'",
						'placeholder': 'Ingrese sus apellidos',
					}
				)
		}

	#validacion de las contraseñas que sean iguales
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Las contraseñas no coinciden!.')
		return password2

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		#if commit sea verdadero o True
		if commit:
			user.save()
		return user

#formulario de editar usuarios
class EditarUsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = {'email','nombres','apellidos','imagen'}
		widgets = {
			'email': forms.EmailInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Correo Electrónico',
					}
				),
			'nombres': forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Ingrese sus nombres',
					}
				),
			'apellidos': forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Ingrese sus apellidos',
					}
				)
		}

#formulario de editar contraseña de usuarios
class EditarPasswordUsuarioForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Contraseña nueva', widget = forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder='Ingrese su contraseña'",
				'placeholder': 'Ingrese su contraseña',
				'id': 'password1',
				'required': 'required',
			}
		))

	password2 = forms.CharField(label = 'Contraseña de confirmacion',widget=forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'onfocus': "this.placeholder = ''",
				'onblur': "this.placeholder='Ingrese nuevamente su contraseña'",
				'placeholder': 'Ingrese nuevamente su contraseña',
				'id': 'password2',
				'required': 'required',
			}
		))
	class Meta:
		model = Usuario
		fields = {}
	#validacion de las contraseñas que sean iguales
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Las contraseñas no coinciden!.')
		return password2

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		#if commit sea verdadero o True
		if commit:
			user.save()
		return user