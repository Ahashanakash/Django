from django.contrib import admin
from .models import transaction

@admin.register(transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'transaction_type', 'amount', 'balance_after_transaction', 'loan_approve', 'timestamp']
    list_filter = ['transaction_type', 'loan_approve', 'timestamp']
    search_fields = ['account__user__username', 'account__account_no', 'transaction_type']
    readonly_fields = ['timestamp']
    
    # Custom actions for loan approval
    actions = ['approve_loans', 'reject_loans']
    
    def approve_loans(self, request, queryset):
        # Only approve loan requests that are not already approved
        loan_requests = queryset.filter(transaction_type='Loan Request', loan_approve=False)
        updated = loan_requests.update(loan_approve=True)
        self.message_user(request, f'{updated} loan(s) have been approved.')
    approve_loans.short_description = "Approve selected loan requests"
    
    def reject_loans(self, request, queryset):
        # Reject loan requests by setting loan_approve to False
        loan_requests = queryset.filter(transaction_type='Loan Request')
        updated = loan_requests.update(loan_approve=False)
        self.message_user(request, f'{updated} loan(s) have been rejected.')
    reject_loans.short_description = "Reject selected loan requests"
    
    # Customize the list view for better loan management
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Add a custom field to show loan status
        return qs
    
    def loan_status(self, obj):
        if obj.transaction_type == 'Loan Request':
            if obj.loan_approve:
                return '✅ Approved'
            else:
                return '⏳ Pending'
        return '-'
    loan_status.short_description = 'Loan Status'