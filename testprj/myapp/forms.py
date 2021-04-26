from django import forms 
from django.core.exceptions import ValidationError

##models internal resources 
from .models import Student,Courses
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','address'
        ,'age']
    # khi nhap moi studen thi khong dc nhap trung first_name, last_name truoc do 
    # la clean_first_name
    # validate cho truong thi tao ham co ten la clean <ten truong> can validate
    def clean_first_name(self):
        print("**** Vo ham cleanData")
        first_name_inputed = self.cleaned_data.get('first_name', None)
        print(first_name_inputed)
        # lay ra success -> first name exist; fail -> not exist 
        try:
            Student.objects.get(first_name=first_name_inputed)
        except Student.DoesNotExist:
            #Student khong ton tai 
            return first_name_inputed
        raise ValidationError(f"{first_name_inputed} da ton tai. vui long nhap ten khac")

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['c_code','c_name','duration'
        ,'begin_date']

class RegisterForm(forms.Form):
    username = forms.CharField(label="user name",max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="password",max_length=20,widget=forms.PasswordInput())
    # confirm_password = forms.CharField(label="confirm_password",max_length=20,widget=forms.PasswordInput())      
    
    email      = forms.EmailField(label="Email")
    first_name = forms.CharField(label="first_name",max_length=20)
    last_name = forms.CharField(label="last_name",max_length=20)

    def clean_username(self):
        # Kiem tra co trung user_name hay khong 
        new_username = self.cleaned_data['username']
        try:
            User.objects.get(username=new_username)
        except User.DoesNotExist:
            return new_username
        raise ValidationError(f"{new_username} da ton tai. vui long chon ten khac")

    def clean_email(self):
        # Kiem tra co trung email hay khong 
        new_email = self.cleaned_data['email']
        try:
            User.objects.get(email=new_email)
        except User.DoesNotExist:
            return new_email
        raise ValidationError(f"{new_email} da ton tai. vui long chon ten khac")
    # def clean_confirm_password(self):
    #     # Kiem tra co trung user_name hay khong 
    #     password = self.cleaned_data["password"]
    #     confirm_password = self.cleaned_data["confirm_password"]
    #     if password != confirm_password:
    #         return ValidationError("NHap lai mat khau khong trung khop")


    def save_user(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            # confirm_password=self.cleaned_data['confirm_password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        ) 

class LoginForm(forms.Form):
    username = forms.CharField(label="user name",max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="password",max_length=20,widget=forms.PasswordInput())
    
    