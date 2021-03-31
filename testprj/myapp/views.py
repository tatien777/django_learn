from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,response 

## models
from .models import Student, Place, Restaurant, Waiter, Article, Publication,Courses
from .forms import StudentForm,CourseForm

# Create your views here.
def index(request):
    # print(req.GET)
    # response = HttpResponse()
    # response.write("<h1> Test H1 </h1>")
    # response.write(f"Hello {req.GET.get('name','')}")
    # response.write(f" session is {req.session.get('name','')}")
    class_name = "python2011E"
    list_studs = ["nguyenA","nguyenB","nguyenC"]
    product_lists = ["A","B","C"]
    return render(
        request=request,
        template_name='index.html',
        context={
            'class_name' : class_name,
            'students': list_studs,
            'productList': product_lists,
        }
    )


def login(req):
    name = req.GET.get('name','')
    req.session['name'] = name 
    return HttpResponse('Logged is as: '+ name)

## Thu tu tao ra 1 views moi 
## Buoc 1: tao ham trong views.py trong <app> django 

def register(request): #request: HTTP request
    hello = ""
    if  request.method == 'POST':
        
        print(request.POST)
        username = request.POST.get('username')
        pw = request.POST.get('password')
        if username != 'admin':
           hello = "thong tin dang nhap khong chinh xac"
        else: 
            hello = f"hello {request.POST.get('username')}"
    return render(
        request=request,
        template_name='register.html',
        context={
            'hello':hello
        }
    )


def list_all_students(request):
    students = Student.objects.all()
    return render(
        request=request,
        template_name='student.html',
        context={
            'students':students
        }

    )
def view_student(request,student_id):
    student = get_object_or_404(Student,id=student_id)
    return render(
        request=request,
        template_name='detail.html',
        context={
            'students':student
        })

def delete_student(request,student_id):
    student = get_object_or_404(Student,id=student_id)
    student.delete()
    return redirect('student')

#Create 
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        if request.is_ajax:
            first_name = request.POST.get('first_name')
            print("call from ajax: ",first_name)
            try:
                Student.objects.get(first_name=first_name)
            except Student.DoesNotExist:
            #Student khong ton tai 
                return response.JsonResponse({
                    'info':'Ok',
                    'status':'200'
                },safe=True)
            return response.JsonResponse({
                    'info':'Bi turng'
                },safe=True)
        # print(request.method)
        else:
            form = StudentForm(request.POST)
            if form.is_valid(): 
                data = form.cleaned_data
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                address = data.get('address')
                age = data.get('age')
                Student.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    address=address,
                )
                return redirect('student')
    return render(
        request=request,
        template_name='add_student.html',
        context = {
            'form':form
        }
    )

#Update 
def edit_student(request,student_id):
    student = Student.objects.get(id=student_id)
    # form = StudentForm(first_name = student.first_name,
    #                     ,last_name = student.last_name,
    #                     ,age = student.age,
    #                     ,address = student.address,)
    return render(
        request=request,
        template_name='edit_student.html',
        context = {
            'student':student
        }
    )


# CREATE 
def create_course(request):
    form = CourseForm()
    form_request = CourseForm(request.POST)
    if form_request.is_valid():
        data = form_request.cleaned_data
        c_code = data['c_code']
        c_name = data['c_name']
        duration = data['duration']
        begin_date = data['begin_date']
        print("data",c_code,c_name,duration,begin_date)
        Courses.objects.create(
            c_code=c_code,
            c_name=c_name,
            duration=duration,
            begin_date=begin_date,
        )
        return redirect('create_course')
    return render(
        request=request,
        template_name='create_course.html',
        context = {'form': form}

    ) 