from .models import OrderReview
from django import forms
from django.utils.translation import gettext_lazy as _

class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order_id', 'reviewer',)
        widgets = {'order_id': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}