from django import forms

from cruise.models import Cruise, Ships


class StyleFormMixin:
    """
    Стиль для отображения формы заполнения
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CruiseForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для изменения круиза
    """

    class Meta:
        model = Cruise
        fields = "__all__"


class ShipForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для изменения теплохода
    """

    class Meta:
        model = Ships
        fields = "__all__"
