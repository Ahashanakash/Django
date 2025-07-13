from dataclasses import fields
from django import forms
from django.http import request
from .models import transaction
from user.models import Profile

class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account', None)
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = transaction
        fields = ['amount']

class AddMoneyForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return amount
        
class CashOutForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance

        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw {amount} $'
            )

        return amount
    
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        min_loan_amount = 500
        max_loan_amount = 50000

        if amount < min_loan_amount:
            raise forms.ValidationError(
                f'You can borrow at least {min_loan_amount} $'
            )

        if amount > max_loan_amount:
            raise forms.ValidationError(
                f'You can borrow at most {max_loan_amount} $'
            )

        return amount
    
    
class TransferForm(TransactionForm):
    recipient_account_no = forms.IntegerField(
        label='Recipient Account Number',
        help_text='Enter reciever account number'
    )
    
    class Meta:
        model = transaction
        fields = [
            'amount',
            'recipient_account_no',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient_account_no'].widget.attrs.update({
            'class': (
                'appearance-none block w-full bg-gray-200 '
                'text-gray-700 border border-gray-200 rounded '
                'py-3 px-4 leading-tight focus:outline-none '
                'focus:bg-white focus:border-gray-500'
            )
        })
    
    def clean_recipient_account_no(self):
        recipient_account_no = self.cleaned_data.get('recipient_account_no')
        
        try:
            recipient_account = Profile.objects.get(account_no=recipient_account_no)
        except Profile.DoesNotExist:
            raise forms.ValidationError('Recipient account not found. Please check the account number.')
        
        if recipient_account == self.account:
            raise forms.ValidationError('You cannot transfer money to your own account.')
        
        return recipient_account_no
    
    def clean_amount(self):
        account = self.account
        min_transfer_amount = 100
        max_transfer_amount = 10000
        balance = account.balance

        amount = self.cleaned_data.get('amount')
        if amount < min_transfer_amount:
            raise forms.ValidationError(
                f'You can transfer at least {min_transfer_amount} $'
            )

        if amount > max_transfer_amount:
            raise forms.ValidationError(
                f'You can transfer at most {max_transfer_amount} $'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not transfer {amount} $'
            )

        return amount

class LoanPayForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_pay_amount = 100
        max_pay_amount = 50000
        balance = account.balance

        amount = self.cleaned_data.get('amount')
        if amount < min_pay_amount:
            raise forms.ValidationError(
                f'You can pay at least {min_pay_amount} $'
            )

        if amount > max_pay_amount:
            raise forms.ValidationError(
                f'You can pay at most {max_pay_amount} $'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not pay {amount} $'
            )

        return amount