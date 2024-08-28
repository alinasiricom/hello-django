from django import forms
from .models import Contact, Newsletter
from captcha.fields import CaptchaField

class ContactForm1(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm2(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'