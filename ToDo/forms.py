from django import forms

class ToDoListForm(forms.Form):
    name = forms.CharField(required=False, label='',
                           widget=forms.TextInput(attrs={'class':'form-control m-auto'}))

class SearchForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control m-auto', 'placeholder':'Search...'}),
                         required=False, label='')
