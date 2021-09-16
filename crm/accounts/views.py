from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from .models import Customer
from .models import Order
from .models import Product
from .forms import OrderForm

# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all().order_by('name')

    context = {'products': products}

    return render(request, 'accounts/products.html', context)


def customers(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_orders
    }

    return render(request, 'accounts/customers.html', context)


def create_order(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, 
        Order, 
        fields=('product', 'status'), 
        extra=5
    )
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})
    # formset = OrderFormSet(instance=customer)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        print('---> Requested order: ', request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    # context = {'form': form}
    context = {'formset': formset}

    return render(request, 'accounts/order_form.html', context)


# pk -> Primary Key
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}

    return render(request, 'accounts/delete.html', context)
