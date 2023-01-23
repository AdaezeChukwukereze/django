from django.shortcuts import render
from bank.models import Bank , Customer

# Create your views here.
def home_page(request):
    banks = Bank.objects.all()
    customers = Customer.objects.all()
    context = {
        "banks": banks,
        "customers" :customers
    }
    return render(request,"bank/Base.html", context)
