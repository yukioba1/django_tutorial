from django.shortcuts import render

def input_num(request):
    return render(request, 'numapp/input_num.html')


def print_msg(request):
    context = {
        'num' : request.POST['num'],
    }
    return render(request, 'numapp/print_msg.html', context)
