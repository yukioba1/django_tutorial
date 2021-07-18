from django.shortcuts import render

def input_num(request):
    return render(request, 'numapp/input_num.html')