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
    # class_name = "python2011E"
    # list_studs = ["nguyenA","nguyenB","nguyenC"]
    # product_lists = ["A","B","C"]
    return render(
        request=request,
        template_name='index.html',
        # context={
        #     'class_name' : class_name,
        #     'students': list_studs,
        #     'productList': product_lists,
        # }
    )
def index_one2one(request):
    return render(
        request=request,
        template_name='one2one.html',
        context={
            'places': places,
            'restaurants':restaurants,
        }
    )

def index_one2many(request):
    return render(
        request=request,
        template_name='one2many.html',
    )

def index_mn2mn(request):
    return render(
        request=request,
        template_name='mn2mn.html',
    )

def login(req):
    name = req.GET.get('name','')
    req.session['name'] = name 
    return HttpResponse('Logged is as: '+ name)

## Thu tu tao ra 1 views moi 
## Buoc 1: tao ham trong views.py trong <app> django 

# def register(request): #request: HTTP request
#     hello = ""
#     if  request.method == 'POST':
        
#         print(request.POST)
#         username = request.POST.get('username')
#         pw = request.POST.get('password')
#         if username != 'admin':
#            hello = "thong tin dang nhap khong chinh xac"
#         else: 
#             hello = f"hello {request.POST.get('username')}"
#     return render(
#         request=request,
#         template_name='register.html',
#         context={
#             'hello':hello
#         }
#     )


# def list_all_students(request):
#     students = Student.objects.all()
#     return render(
#         request=request,
#         template_name='student.html',
#         context={
#             'students':students
#         }

#     )
# def view_student(request,student_id):
#     student = get_object_or_404(Student,id=student_id)
#     return render(
#         request=request,
#         template_name='detail.html',
#         context={
#             'students':student
#         })

# def delete_student(request,student_id):
#     student = get_object_or_404(Student,id=student_id)
#     student.delete()
#     return redirect('student')

# #Create 
# def add_student(request):
#     form = StudentForm()
#     if request.method == 'POST':
#         if request.is_ajax:
#             first_name = request.POST.get('first_name')
#             print("call from ajax: ",first_name)
#             try:
#                 Student.objects.get(first_name=first_name)
#             except Student.DoesNotExist:
#             #Student khong ton tai 
#                 return response.JsonResponse({
#                     'info':'Ok',
#                     'status':'200'
#                 },safe=True)
#             return response.JsonResponse({
#                     'info':'Bi turng'
#                 },safe=True)
#         # print(request.method)
#         else:
#             form = StudentForm(request.POST)
#             if form.is_valid(): 
#                 data = form.cleaned_data
#                 first_name = data.get('first_name')
#                 last_name = data.get('last_name')
#                 address = data.get('address')
#                 age = data.get('age')
#                 Student.objects.create(
#                     first_name=first_name,
#                     last_name=last_name,
#                     age=age,
#                     address=address,
#                 )
#                 return redirect('student')
#     return render(
#         request=request,
#         template_name='add_student.html',
#         context = {
#             'form':form
#         }
#     )

#Update 
# def edit_student(request,student_id):
#     student = Student.objects.get(id=student_id)
#     # form = StudentForm(first_name = student.first_name,
#     #                     ,last_name = student.last_name,
#     #                     ,age = student.age,
#     #                     ,address = student.address,)
#     return render(
#         request=request,
#         template_name='edit_student.html',
#         context = {
#             'student':student
#         }
#     )



##### ADD VIEW ##### 

from django.views import View 
from django.views.generic import ListView

from django.core.paginator import Paginator

def all_students(request):
    students = Student.objects.all()
    first_name = request.GET.get('first_name')
    if first_name:
        students = students.filter(first_name__contains=first_name)


    paginator = Paginator(students,3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(
        request=request,
        template_name='test_students.html',
        context={
            'page_obj': page_obj,
            'students':students,
        }
        )


class StudentListView(ListView):
    model = Student
    template_name = 'list_students.html'
    form = StudentForm()
    paginate_by = 3 #so luong itme muon hien thi


## detail view
from django.views.generic.detail import DetailView
from django.utils import timezone

class StudentDetailView(DetailView):
    model = Student
    template_name = 'detail_students.html'
    
    def get_queryset(self,model=model):
        first_name = self.kwargs.get('first_name', None)
        object_list = model.objects.all()
        if first_name:
            object_list = object_list.filter(first_name__icontains=first_name)
        return object_list
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


## Create View ## 
from django.views.generic.edit import CreateView
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'create_student.html'
    success_url =  '/student'


## Update View ## 
from django.views.generic.edit import UpdateView
class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'edit_student.html' 
    success_url =  '/student'


## Delete View ## 
from django.views.generic.edit import DeleteView
class StudentDeleteView(DeleteView):
    model = Student
    fields = '__all__'
    template_name = 'delete_student.html' 
    success_url =  '/student'





# CREATE 
# def create_course(request):
#     form = CourseForm()
#     form_request = CourseForm(request.POST)
#     if form_request.is_valid():
#         data = form_request.cleaned_data
#         c_code = data['c_code']
#         c_name = data['c_name']
#         duration = data['duration']
#         begin_date = data['begin_date']
#         print("data",c_code,c_name,duration,begin_date)
#         Courses.objects.create(
#             c_code=c_code,
#             c_name=c_name,
#             duration=duration,
#             begin_date=begin_date,
#         )
#         return redirect('view_course')
#     return render(
#         request=request,
#         template_name='create_course.html',
#         context = {'form': form}

#     ) 
# # READ COURSE AND STUDENT 
# def view_course(request):
    
#     courses = Courses.objects.all()
#     print(courses[0].c_num)
#     return render(
#         request=request,
#         template_name='view_course.html',
#         context = {'courses': courses}

#     ) 
# # UPDATE COURSE  
# def edit_course(request,code):
#     course = Courses.objects.get(c_code=code)
#     # print("code he thog",code)
#     print("code query",course.begin_date)
#     if request.method == 'POST':
#         c_name = request.POST.get('c_name')
#         duration = request.POST.get('duration')
#         begin_date = request.POST.get('begin_date')
#         print("***",c_name,duration,begin_date)
#         course.c_name = c_name
#         course.duration = duration
#         course.begin_date = begin_date
#         course.save()
#     return render(
#         request=request,
#         template_name='edit_course.html',
#         context = {
#             'course': course,
#         }

#     ) 

# #DELETE
# def delete_course(request,code):
#     course = get_object_or_404(Courses,c_code=code)
#     course.delete()
#     return redirect('view_course')

class CourseListView(ListView):
    model = Courses
    template_name = 'list_courses.html'
    # form = CourseForm()
    paginate_by = 2 #so luong itme muon hien thi


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'detail_course.html'
    
    def get_queryset(self,model=model):
        c_code = self.kwargs.get('c_code', None)
        object_list = model.objects.all()
        if c_code:
            object_list = object_list.filter(c_code__icontains=c_code)
        return object_list
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CourseCreateView(CreateView):
    # def __init__(self, *args, **kwargs):
    #     super(CourseCreateView, self).__init__(*args, **kwargs)
    #     if not self.instance:
    #         self.fields.pop('c_num')
    model = Courses
    fields = ['c_code','c_name','duration','begin_date']
    template_name = 'create_course.html'
    success_url =  '/course'

class CourseUpdateView(UpdateView):
    model = Courses
    fields = '__all__'
    template_name = 'edit_course.html' 
    success_url =  '/course'

class CourseDeleteView(DeleteView):
    model = Courses
    fields = '__all__'
    template_name = 'delete_course.html' 
    success_url =  '/course'