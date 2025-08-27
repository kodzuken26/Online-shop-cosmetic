from django.shortcuts import render

# def base_view(request):
#     return render(request, 'main/base.html')

def main_view(request):
    return render(request, 'main/main.html')