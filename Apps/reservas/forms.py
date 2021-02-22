from django import forms
from .models import ReservaDeporte, ReservaHotel

class ReservaDeporteForm(forms.ModelForm):
	class Meta:
		model = ReservaDeporte
		fields = ['fecha_inicial','fecha_final']

class ReservaHotelForm(forms.ModelForm):
	class Meta:
		model = ReservaHotel
		fields = ['fecha_inicial','fecha_final']