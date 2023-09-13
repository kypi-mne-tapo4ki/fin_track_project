from django import forms

from .models import Operation, Category, CategoryType, Tag


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['user', 'source', 'destination', 'amount', 'tag']
        widgets = {
            'tag': forms.CheckboxSelectMultiple,
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user', 'title', 'category_type']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'binding']
