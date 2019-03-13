from django import forms

class AddFactoryForm(forms.Form):
    name = forms.CharField(max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder' : 'Factory Name', 'name' : 'name', 'required' : ''}))
    minimum = forms.IntegerField(
            widget=forms.TextInput(
                attrs={'placeholder' : 'Minimum Number', 'name' : 'minimum', 'required' : ''}))
    maximum = forms.IntegerField(
            widget=forms.TextInput(
                attrs={'placeholder' : 'Maximum Number', 'name' : 'maximum', 'required' : ''}))
    children = forms.IntegerField(
            widget=forms.TextInput(
                attrs={'placeholder' : 'Number of Children', 'name' : 'children', 'min' : '0', 'max' : '15', 'required' : ''}))

class EditFactoryForm(forms.Form):

    select = forms.CharField(max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder' : 'Which Factory?', 'name' : 'select', 'value' : 'none', 'required' : ''}))
    name = forms.CharField(max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder' : 'Factory Name', 'name' : 'name', 'value' : 'none', 'required' : ''}))
    minimum = forms.IntegerField(
            widget=forms.TextInput(
                attrs={'placeholder' : 'Minimum Number', 'name' : 'minimum', 'value' : 'none', 'required' : ''}))
    maximum = forms.IntegerField(
            widget=forms.TextInput(
                attrs={'placeholder' : 'Maximum Number', 'name' : 'maximum', 'value' : 'none', 'required' : ''}))

class DeleteFactoryForm(forms.Form):
    select = forms.CharField(max_length=30,
            widget=forms.TextInput(
                attrs={'placeholder' : 'Which Factory?', 'name' : 'select', 'required' : ''}))
