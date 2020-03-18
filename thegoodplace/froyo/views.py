from django.shortcuts import render

def ingredients_list(request):
    return render(request, 'ingredients_list.html')