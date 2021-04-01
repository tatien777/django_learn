from models import Student,Courses

c1 = Courses.objects.get(c_code="DA-2102")
print(c1)