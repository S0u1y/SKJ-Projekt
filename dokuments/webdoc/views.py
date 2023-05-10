from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

from .models import *

from .forms import *


# Create your views here.


def index(request):
    documents = Document.objects.all()
    return render(request, 'webdoc/index.html',
                  {'documents': documents})


def documentmain(request, document_id):
    document = Document.objects.get(pk=document_id)
    comments = Comment.objects.filter(document=document)  # why filter? I dunno!

    comment_forms = CommentForm()

    return render(request, 'webdoc/document.html',
                  {'document': document, 'comments': comments, 'comment_form': comment_forms})


def addcomment(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_content = comment_form.cleaned_data['content']
            user = comment_form.cleaned_data['user']
            comment = Comment(document=document, user=user, content=comment_content)
            comment.save()

    return redirect('document', document_id=document.id)


def page(request, document_id, page_num):
    document = Document.objects.get(pk=document_id)
    page = Page.objects.get(document=document, page_number=page_num)

    return render(request, 'webdoc/page.html', {'page': page})


def login(request):
    if request.method != 'POST':
        return render(request, 'webdoc/login.html')

    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.get(email=email)

    if user is None:
        return redirect('login')
    if user.password == password:
        return redirect('index')
    else:
        return redirect('login')


def register(request):
    user_forms = UserForm()
    return render(request, 'webdoc/register.html', {'user_form': user_forms})


def registeruser(request):
    if request.method != 'POST':
        return redirect('register')

    user_form = UserForm(request.POST)
    if user_form.is_valid():
        name = user_form.cleaned_data.get('name')
        sur_name = user_form.cleaned_data.get('surname')
        address = user_form.cleaned_data.get('address')
        password = user_form.cleaned_data.get('password')
        phone = user_form.cleaned_data.get('phone')
        email = user_form.cleaned_data.get('email')

        newUser = User(name=name, surname=sur_name, address=address, password=password, phone=phone, email=email)
        newUser.save()
        pass

    return redirect('index')


def info(request):
    return render(request, 'webdoc/info.html')


def contacts(request):
    staff = User.objects.filter(permission='Z')
    return render(request, 'webdoc/contacts.html', {'staff': staff})


def payment(requrest):
    payment_form = PaymentForm()
    return render(requrest, 'webdoc/payment.html', {'payment_form': payment_form})


def makepayment(request):
    if request.method != 'post':
        payment_form = PaymentForm()
        return render(request, 'webdoc/payment.html', {'payment_form': payment_form})

    payment_form = PaymentForm(request.POST)
    if payment_form.is_valid():
        payment = Payment(
            user=payment_form.cleaned_data.get('user'),
            amount=payment_form.cleaned_data.get('amount')
        )
        payment.save()

    return redirect('payment')


# TODO create documents?

def addresses(request):
    l_addresses = Address.objects.all()
    address_form = AddressForm()
    return render(request, 'webdoc/addresses.html', {'addresses': l_addresses, 'address_form': address_form})


def makeaddress(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            newAddress = Address(name = address_form.cleaned_data.get('name'))
            newAddress.save()

    return redirect('addresses')
    pass
