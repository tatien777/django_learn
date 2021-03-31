from django import forms 
from django.core.exceptions import ValidationError

##models internal resources 
from .models import Student,Courses


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

