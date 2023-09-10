from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Mahoga Aribowo Heryasa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)