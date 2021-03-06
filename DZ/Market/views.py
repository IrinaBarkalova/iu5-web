from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.shortcuts import render, get_object_or_404
from .models import Store, Product


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    return render(request,
                  'product/detail.html',
                  {'product': product})


def product_list(request, store_slug=None):
    store = None
    stores = Store.objects.all()
    products = Product.objects.all()
    if store_slug:
        store = get_object_or_404(Store, slug=store_slug)
        products = products.filter(store=store)
    return render(request,
                  'product/list.html',
                  {'store': store,
                   'stores': stores,
                   'products': products})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

