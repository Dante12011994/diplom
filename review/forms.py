from django import forms

from review.models import Review
from cruise.forms import StyleFormMixin


class ReviewForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания и изменения статей отзыва
    """
    class Meta:
        model = Review
        fields = "__all__"
