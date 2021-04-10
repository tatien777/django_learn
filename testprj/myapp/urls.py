from django.conf.urls import url 
from django.urls import path

from . import views 

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^one-one$',views.index_one2one,name="index_one2one"),
    url(r'^one-many$',views.index_one2many,name="index_one2many"),
    url(r'^many-many$',views.index_mn2mn,name="index_mn2mn"),



    # url(r'^login$',views.login,name="login"),
    # url(r'^register$',views.register,name="register"),
    url(r'^student/$',view=views.StudentListView.as_view(),name="list_students"),
    # # url(r'^student/(?P<student_id>[0-9]+)$',view=views.view_student,name="view_student"),
    path('student/<pk>',view=views.StudentDetailView.as_view(),name="detail_students"),
    path('edit_student/<pk>',view=views.StudentUpdateView.as_view(),name="edit_student"),
    path('delete_student/<pk>',view=views.StudentDeleteView.as_view(),name="delete_student"),
    url(r'^add_student/$',view=views.StudentCreateView.as_view(),name="add_student"),
    # url(r'^create_course/$',view=views.create_course,name="create_course"),
    url(r'^view_course/$',view=views.view_course,name="view_course"),

    path('view_course/<c_code>',view=views.view_course,name="view_course"),
    path('edit_course/<code>',view=views.edit_course,name="edit_course"),
    path('delete_code/<code>',view=views.delete_course,name="delete_course"),
]


