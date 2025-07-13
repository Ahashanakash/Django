from django.db import models
from user.models import Profile

# Create your models here.
class transaction(models.Model):
    account = models.ForeignKey(Profile, related_name = 'transactions', on_delete = models.CASCADE)
    receiver = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['timestamp']
        
    def __str__(self):
        return str(self.transaction_type)