from django.shortcuts import render

def home(request):
    context = {
        'is_staff': request.user.groups.filter(name="Staff").exists() if request.user.is_authenticated else False,
        'is_superuser': request.user.is_superuser if request.user.is_authenticated else False,
    }
    return render(request, 'Web/home.html', context)
