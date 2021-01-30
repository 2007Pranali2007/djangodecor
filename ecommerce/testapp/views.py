from django.shortcuts import render,redirect
from django.views.generic import DetailView
from testapp.models import Product
from testapp.forms import ConfirmationForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import authenticate, login, logout

# Create your views here.
'''def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/accounts/login')
        my_dict = {'form': form}
        return render(request, "acc/register.html", my_dict)'''

'''def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'signup/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/register')'''



@login_required
def read_data(request):
    product_list=Product.objects.all()

    item_name=request.GET.get('item_name')#laptop
    if item_name!='' and item_name is not None:
        product_list=product_list.filter(name__contains=item_name)



    my_dict={'product_list':product_list}
    return render(request,"welcome.html",my_dict)


class Read_One_Data(DetailView):
    model=Product
    #default template name:product_detail.html
    #default context variable:product or object

def checkout_view(request):
    checkout(request)
    return render(request,"checkout.html")

@login_required
def confirm_view(request):
    form=ConfirmationForm()
    my_dict={'form':form}

    if request.method=='POST':
        form=ConfirmationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/success')


    #return render(request,"checkout.html",my_dict)
    return render(request,"order.html",my_dict)

@login_required
def successful_view(request):
    return render(request,"success.html")
