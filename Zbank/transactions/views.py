from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from transactions.models import transaction
from user.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def AddMoney(request):
    if request.method=='POST':
        form = forms.AddMoneyForm(request.POST, account=request.user.account)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            account = request.user.account
            account.balance += amount
            account.save()
            
            # Create transaction record
            transaction.objects.create(
                account=account,
                amount=amount,
                balance_after_transaction=account.balance,
                transaction_type='Add Money'
            )
            
            messages.success(request,'Add money successful.')
            return redirect('home')
    else:
        form = forms.AddMoneyForm(account=request.user.account)
    return render(request, 'transaction.html', {'data': form, 'type':'Add Money'})

@login_required
def Cashout(request):
    if request.method=='POST':
        form = forms.CashOutForm(request.POST, account=request.user.account)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            account = request.user.account
            account.balance -= amount
            account.save()
            
            # Create transaction record
            transaction.objects.create(
                account=account,
                amount=amount,
                balance_after_transaction=account.balance,
                transaction_type='Cash Out'
            )
            
            messages.success(request,'Cash Out successful.')
            return redirect('home')
    else:
        form = forms.CashOutForm(account=request.user.account)
    return render(request, 'transaction.html', {'data': form, 'type':'Cash Out'})

@login_required
def SendMoney(request):
    if request.method=='POST':
        form = forms.TransferForm(request.POST, account=request.user.account)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            recipient_account_no = form.cleaned_data.get('recipient_account_no')
            account = request.user.account
            recipient_account = Profile.objects.get(account_no=recipient_account_no)
            
            # Update balances
            account.balance -= amount
            recipient_account.balance += amount
            account.save()
            recipient_account.save()
            
            # Create transaction records
            transaction.objects.create(
                account=account,
                receiver=recipient_account_no,
                amount=amount,
                balance_after_transaction=account.balance,
                transaction_type='Send Money'
            )
            
            messages.success(request,'Send money successful.')
            return redirect('home')
    else:
        form = forms.TransferForm(account=request.user.account)
    return render(request, 'sendMoney.html', {'data': form, 'type':'Send Money'})

@login_required
def Loan(request):
    if request.method=='POST':
        form = forms.LoanRequestForm(request.POST, account=request.user.account)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            account = request.user.account
            account.save()
            
            # Create transaction record
            transaction.objects.create(
                account=account,
                amount=amount,
                balance_after_transaction=account.balance,
                transaction_type='Loan Request'
            )
            
            messages.success(request,'Loan request successful.')
            return redirect('home')
    else:
        form = forms.LoanRequestForm(account=request.user.account)
    return render(request, 'transaction.html', {'data': form, 'type':'Loan Request'})


@login_required
def transaction_history(request):
    """Display all transaction history for the current user"""
    account = request.user.account
    
    # Get all transactions for this user, ordered by timestamp (newest first)
    transactions = transaction.objects.filter(
        account=account
    ).order_by('-timestamp')
    
    # Calculate summary statistics
    total_transactions = transactions.count()
    total_deposits = sum(t.amount for t in transactions if t.transaction_type == 'Add Money')
    total_withdrawals = sum(t.amount for t in transactions if t.transaction_type == 'Cash Out')
    total_transfers = sum(t.amount for t in transactions if t.transaction_type == 'Send Money')
    pending_loans = transactions.filter(transaction_type='Loan Request', loan_approve=False).count()
    
    return render(request, 'transaction_history.html', {
        'transactions': transactions,
        'type': 'Transaction History',
        'summary': {
            'total_transactions': total_transactions,
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals,
            'total_transfers': total_transfers,
            'pending_loans': pending_loans,
            'current_balance': account.balance,
        }
    })
    
@login_required
def PendingLoans(request):
    """Display all pending loans for the current user"""
    account = request.user.account
    
    # Get all pending loan requests for this user (both unapproved and approved but unpaid)
    pending_loans = transaction.objects.filter(
        account=account,
        transaction_type='Loan Request'
    ).order_by('-timestamp')
    
    # Separate unapproved and approved loans
    unapproved_loans = pending_loans.filter(loan_approve=False)
    approved_loans = pending_loans.filter(loan_approve=True)
    
    # Calculate summary statistics
    total_loan_amount = sum(loan.amount for loan in approved_loans)
    payable_loans = sum(1 for loan in approved_loans if account.balance >= loan.amount)
    
    return render(request, 'pending_loans.html', {
        'unapproved_loans': unapproved_loans,
        'approved_loans': approved_loans,
        'type': 'Pending Loans',
        'summary': {
            'total_loan_amount': total_loan_amount,
            'payable_loans': payable_loans,
            'current_balance': account.balance,
            'unapproved_count': unapproved_loans.count(),
            'approved_count': approved_loans.count(),
        }
    })

@login_required
def LoanPay(request, loan_id):
    if request.method=='POST':
        account = request.user.account
        
        # Get the specific loan transaction by ID (must be approved)
        try:
            loan_transaction = transaction.objects.get(
                id=loan_id,
                account=account,
                transaction_type='Loan Request',
                loan_approve=True  # Only approved loans can be paid
            )
            
            loan_amount = loan_transaction.amount
            
            # Check if user has enough balance to pay the loan
            if account.balance >= loan_amount:
                account.balance -= loan_amount
                account.save()
                
                # Mark the loan as paid by changing transaction type
                loan_transaction.transaction_type = 'Loan Paid'
                loan_transaction.save()
                
                # Create transaction record for loan payment
                transaction.objects.create(
                    account=account,
                    amount=loan_amount,
                    balance_after_transaction=account.balance,
                    transaction_type='Loan Paid'
                )
                
                messages.success(request, f'Loan payment of ${loan_amount} successful.')
                return redirect('pending_loans')
            else:
                messages.error(request, f'Insufficient balance. You need ${loan_amount} to pay the loan.')
                return redirect('pending_loans')
                
        except transaction.DoesNotExist:
            messages.error(request, 'Loan not found or not approved for payment.')
            return redirect('pending_loans')
    
    return redirect('pending_loans')
    