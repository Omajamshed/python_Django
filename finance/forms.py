from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from finance.models import Transaction,Goal

class RegisterForm(UserCreationForm):
    # kon sa model us krna h wo is may liktay hain
    first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']


        


class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=['title','amount','transaction_type','date','category']
        
class GoalForm(forms.ModelForm):
    class Meta:
        model= Goal
        fields=['user','target_amount','deadline','name','current_amount']
        exclude = ['user'] 
        
