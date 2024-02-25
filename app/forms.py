from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=50)
    password = forms.CharField(label="password", max_length=50)


class QueryForm(forms.Form):
    keyword = forms.CharField(required=False)
    industry = forms.CharField(required=False)
    year_founded = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    employee_from = forms.CharField(required=False)
    employee_to = forms.CharField(required=False)
