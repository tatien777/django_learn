import os 
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE","testprj.settings")
django.setup()

print("SETUP success")

# from myapp.models import Student,Place,Restaurant 

# ## lay tat ca cac models 
# students = Student.objects.all()

# for std in students:
#     print(std)

# print("*"*20)
# # Lay data co dieu kien tra ve 1 list data
# ## .filter(ten trunong dieu kien )

# stud_contain = Student.objects.filter(last_name__contains="Nguyen")
# for std in stud_contain: 
#     print("student with name 'Nguyen' ", std)

# print("*"*20)


# from myapp.models import Place, Restaurant, Waiter

# place = Place.objects.get(id=1)
# res = Restaurant.objects.get(pk=1) 

# w1 = Waiter(restaurant=res,name="Waiter1")
# w1.save()
# print(w1)


from myapp.models import Student,Courses

c1 = Courses.objects.all()
print(c1)
# s1 = Student.objects.get(id=4)
# print(s1)
# c1.c_num.add(s1.id)
# c1.save()


