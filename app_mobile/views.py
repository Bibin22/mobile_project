from django.shortcuts import render, redirect, HttpResponse
from .models import Mobile,Order,Cart
from .forms import UserRegistrationForm, OrderCreateForm, OrderSubmitForm, CreatMobileForm, FilterForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def user_registration(request):
    form = UserRegistrationForm()
    context = {
        "form":form,
    }
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            form = UserRegistrationForm()
            context = {
                "form":form,
            }
            return render(request, 'app_mobile/registration.html', context)
    return render(request, 'app_mobile/registration.html', context)

def user_signin(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view')
        else:
            return render(request, 'app_mobile/login.html',{"message":"invalid usernam or password"})
    return render(request, 'app_mobile/login.html')

def user_signout(request):
    logout(request)
    return redirect('signin')

def create_mobiles(request):
    form = CreatMobileForm()
    context = {
        "form":form,
    }
    if request.method == "POST":

        form = CreatMobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminview')
        else:
            context = {
                "form": form
            }
            return render(request, 'app_mobile/admin_create.html', context)
    return render(request, 'app_mobile/admin_create.html', context)

def update_mobiles(request, id):
    mobile = Mobile.objects.get(id=id)
    form = CreatMobileForm(instance=mobile)
    context = {
        "form":form,
    }
    if request.method == 'POST':
        form = CreatMobileForm(request.POST, request.FILES, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('adminview')
        else:
            form = CreatMobileForm(request.POST, request.FILES, instance=mobile)
            context = {
                "form":form,
            }
            return render(request, 'app_mobile/admin_create.html', context)
    return render(request, 'app_mobile/admin_create.html', context)

def delete_mobiles(request, id):
    mobile = Mobile.objects.get(id=id)
    mobile.delete()
    return redirect('adminview')

def admin_viewmobiles(request):
    mobiles = Mobile.objects.all()
    paginator = Paginator(mobiles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render (request, 'app_mobile/admin_viewmobiles.html', context)

@login_required()
def view_mobiles(request):
    mobiles = Mobile.objects.all()
    paginator = Paginator(mobiles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render (request, 'app_mobile/first_view.html', context)
@login_required()
def view_details(request, id):
    mobiles = Mobile.objects.get(id=id)
    context = {
        "mobiles":mobiles,
    }
    return render(request, 'app_mobile/viewmobiles.html', context)
@login_required()
def place_order(request, id):
    products = Mobile.objects.get(id=id)
    model_name = products.model_name
    price = products.price
    form = OrderCreateForm(initial={"model_name":model_name, "price":price, "user":request.user})
    context = {

        "form":form
    }
    if request.method == "POST":

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myorder')
        else:
            context = {
                "form":form
            }
            return render(request, 'app_mobile/place_order.html', context)

    return render(request, 'app_mobile/place_order.html', context)

def view_orderline(request):
    orders = Order.objects.all()
    context = {
        "orders":orders
    }
    return render(request, 'app_mobile/admin_orders.html',context)

def view_orders(request, id):
    orders = Order.objects.get(id=id)
    form = OrderSubmitForm(instance=orders)
    context = {
        "form":form
    }
    if request.method == "POST":
        form = OrderSubmitForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            form = OrderSubmitForm(request.POST, instance=orders)
            context = {
                "form":form
            }
            return render(request, 'app_mobile/adminorders.html', context)

    return render(request, 'app_mobile/adminorders.html', context)

@login_required()
def my_order(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        "orders":orders
    }
    return render(request,'app_mobile/my_order.html',context)

@login_required()
def my_orders(request,id):
    orders = Order.objects.get(id=id)
    model_name = orders.model_name
    mobiles = Mobile.objects.get(model_name=model_name)
    context = {
        "orders":orders,
        "mobiles":mobiles
    }

    return render(request,'app_mobile/my_orders.html',context)

@login_required()
def cancel_orders(request, id):
    order = Order.objects.get(id=id)
    if order.status == "order dispatched":
        return redirect('my_order')
    else:
        order.delete()
        return redirect('myorder')

@login_required()
def check_status(request, id):
    order = Order.objects.get(id=id)
    context = {
        "order":order,
    }
    return render(request, 'app_mobile/status.html',context)

@login_required()
def filter(request):
    form = FilterForm()
    context = {
        "form":form,
    }
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            fil = form.cleaned_data.get("filter")
            #print(fil)
            products = Mobile.objects.filter(price__lte=fil)
            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                "form":form,
                "page_obj": page_obj,
            }
    return render(request, 'app_mobile/filter.html',context)

@login_required()
def add_toCart(request, id):

    if request.method == "POST":
        products = Mobile.objects.get(id=id)
        brand_name = products.brand_name
        items = Cart(user=request.user, mobile_id=products)
        items.save()


    return redirect('mycart')

def view_cart(request):
    carts = Cart.objects.filter(user=request.user)

    mobiles = Mobile.objects.filter(model_name__in=[c.mobile_id for c in carts])

    print(carts)
    paginator = Paginator(mobiles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'app_mobile/cart.html', context)

def delete_cart(request, id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('mycart')


def search(request):
    srch = request.GET['search']
    products = Mobile.objects.filter(brand_name=srch)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'app_mobile/search.html', context)








