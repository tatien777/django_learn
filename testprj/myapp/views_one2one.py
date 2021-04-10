# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse,response 

# ## models
# from .models import Place,Restaurant
# from .forms import StudentForm,CourseForm

# ## index 
# def list_all(request):
#     places = Place.objects.all()
#     restaurants = Restaurant.objects.all()
#     return render(
#         request=request,
#         template_name="one2one/list.html",
#         context={
#             'places': places,
#             'restaurants':restaurants,
#         }
#     )