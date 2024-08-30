from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    """
    Newsletter member field
    """
    class Meta:
        model = Member
        fields = ('email',)
