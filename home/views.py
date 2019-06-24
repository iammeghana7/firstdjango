from django.shortcuts import render,redirect
from .forms import CustomForms,SearchForm
from home.models import Book
from django.utils import timezone
from home.forms import ModelBookForms,LoginModelForm
from django.contrib import messages
# from .models import Book


# Create your views here.

def form_view(request):
    msg=''
    form=''
    if request.method == 'POST':
        form=CustomForms(request.POST)
        if form.is_valid():
            # book=Book(   
            #     name=form.cleaned_data.get('name'),
            #     purchase_date=form.cleaned_data.get('purchase_date'),
            #     book_author=form.cleaned_data.get('book_author')
            # )

            book=Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('purchase_date'),
                # genre=form.cleaned_data.get('genre'),
                book_author=form.cleaned_data.get('book_author'),
            )
            book.save()
            msg="Book Added Successfully"
        else:
            msg=form.errors
    else:
        form=CustomForms()
    return render(request,'form.html',{"msg":msg,"forms":form})


def model_form(request):
    msg=''
    if request.method=='POST':
        form=model_form(request.POST)
        if form.is_valid():
            form.save()
            msg='Book Added Successfully'
        else:
            msg=form.errors
    else:
        form=ModelBookForms()

    return render(request,'form.html',{"msg":msg,"forms":form})

def html_form(request):
    value=''
    if request.method=='POST':
        value=request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        value='Wrong input'
    return render(request,'design.html')


def booksearch(request):
    book=''
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            # book=Book.objects.filter(name__contains=q,purchase_date__lte==timezone.now)lte->less than or equals
            form=None
            return render(request,'showtables.html',{'book':book,'form':SearchForm})
    else:
        form=SearchForm()
        book=Book.objects.all()
    
    return render(request,'showtables.html',{'book':book,'form':form})


def deletebook(request,id):
    #with the help of id we delete
    book=Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted' +str(id) +'Successfully')
    return redirect('/')

def editbook(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully')
            return redirect('/')
    else:
        form=ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})
 

def LoginForm(request):
    form=None
    form=LoginModelForm(request.POST)
    print(form)
    if form.is_valid():
        form.save()
    form=LoginModelForm()
    return render(request,'login.html',{'form':form})
