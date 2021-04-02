from django.conf.urls import url 
from django.urls import path

from . import views 

urlpatterns = [
    url(r'^index$',views.index,name="index"),
    url(r'^login$',views.login,name="login"),
    url(r'^register$',views.register,name="register"),
    url(r'^student/$',view=views.list_all_students,name="student"),
    # url(r'^student/(?P<student_id>[0-9]+)$',view=views.view_student,name="view_student"),
    path('student/<int:student_id>',view=views.view_student,name="view_student"),
    path('edit/<int:student_id>',view=views.edit_student,name="edit_student"),
    path('delete/<int:student_id>',view=views.delete_student,name="delete_student"),
    url(r'^add_student/$',view=views.add_student,name="add_student"),
    url(r'^create_course/$',view=views.create_course,name="create_course"),
    url(r'^view_course/$',view=views.view_course,name="view_course"),

    path('view_course/<c_code>',view=views.view_course,name="view_course"),
    path('edit_course/<code>',view=views.edit_course,name="edit_course"),
    path('delete_code/<code>',view=views.delete_course,name="delete_course"),
]


