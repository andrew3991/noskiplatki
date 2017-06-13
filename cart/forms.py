from django import forms


# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
SIZE_CHOICES = (
	('',''),
	(1, '35-38'),
	(2, '39-42'),
	(3,'43-45'),
)
class CartAddProductForm(forms.Form):
	quantity = forms.IntegerField(label="Количество", min_value=1)
	size = forms.TypedChoiceField(label="Количество",choices=SIZE_CHOICES)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)