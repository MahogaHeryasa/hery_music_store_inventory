from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application_name': 'Hery Music Store Inventory',
        'name': 'Mahoga Aribowo Heryasa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)