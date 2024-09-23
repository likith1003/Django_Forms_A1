from django import forms

c = [
    ['Python', 'Py'],
    ['Java', 'Java'],
    ['MERN', 'MERN']
]
g = [
    ['Male', 'Male'],
    ['Female', 'Female'],
    ['Others', 'Others']
]
class DataForm(forms.Form):
    name = forms.CharField(max_length=150 , required=True)
    pno = forms.CharField(max_length=150, required=True)
    email = forms.CharField(max_length=150, required=False)
    add = forms.CharField(max_length=150, required=False)
    cources = forms.ChoiceField(choices=c,  required=False)
    gender=forms.ChoiceField(choices=g, required=False, widget=forms.RadioSelect)
    un = forms.CharField(max_length=150, required=False)
    pw = forms.CharField(max_length=150, required=False)