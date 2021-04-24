from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect,render

def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('list_students')
    return render(
        request=request,
        template_name="user/register.html",
        context={
            'form':form
        },
        )