from django import forms
from trombinoscoop.models import Personne

class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel :')
    password = forms.CharField(label='Mot de passe :', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        # Vérifie que les deux champs sont valides
        if email and password:
            result = Personne.objects.filter(mot_de_passe=password,couriel=email)
            if len(result) != 1:
                raise forms.ValidationError("Adresse de courriel ou mot de passe erroné.")

        return cleaned_data


class PersonneProfileForm (forms.ModelForm):
    class Meta:
        model = Personne
        exclude = ()

