from django import forms
from home.models import Book,Author,Genre,Login
from django.http import HttpResponse,Http404

class CustomForms(forms.Form):
    name=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength' : '30' ,'id':'name','placeholder ':'Book-NAme','class':'form-control'}))
    
    book_author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name': 'book_author','id' : 'book_author','class':'custom-select'}))
    
    purchase_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'Purchase Date','name':'date','id':'purchase_date','class':'form-control'}))



class ModelBookForms(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','genre','purchase_date','author')
    name=forms.CharField(label='Book Name',
        widget=forms.TextInput(attrs={'maxlength' : '30' ,'placeholder ':'Book-NAme','class':'form-control'}))

    book_author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name': 'book_author','id' : 'author','class':'custom-select'}))
    summary=forms.CharField(label='Summary',widget=forms.Textarea(attrs={'placeholder':'Summary','name':'summary','id':'summary',
            'class' :' form-control'}))
    isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'ISBN number','class':'form-control',
    'name':'isbn','id':'isbn'}))

    class Meta:
        model=Book 
        fields='__all__'


class SearchForm(forms.Form):
    q=forms.CharField(label='',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'search','class':'form-control','minlength':'2'}))


class LoginForm(forms.Form):
    Username=forms.CharField(max_length=30)
    email=forms.CharField(max_length=50)
    password=forms.CharField(max_length=30)

class LoginModelForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'max_length':'30','id':'username','class':'form-control'}))
        email=forms.CharField(label='email',widget=forms.TextInput(attrs={'max_length':'30','id':'email','class':'form-control'}))
        password=forms.CharField(label='password',widget=forms.TextInput(attrs={'max_length':'30','id':'password','class':'form-control'}))


    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        print(email)
        print('Im here')
        # {{ wrapping|slice:":-3" }}
        # print({{ email|slice:":-3" }})
        print("Im also here")
        if  (email.endswith(".com")):
            return email
    
        else:
            raise Http404('Email not found')
            # return HttpResponse("Error in email.Please enter valid email")
# class CustomForms (forms.Form):
#     username = forms.CharField(
#         label='Username',
#         widget=forms.TextInput(
#             attrs={ 'placeholder' : 'Your username',
#             'class' : 'form-control','max':'20'}
#         )
#     )   
#     email = forms.EmailField(label="Your Email",widget=forms.EmailInput(attrs={ 'placeholder':'ac@gmail.com','class':'form-control'}))