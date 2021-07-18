from django.shortcuts import render

def input_num(request):
    return render(request, 'numapp/input_num.html')


def print_msg(request):
    context = {
        'num' : request.POST['num'],
    }
    return render(request, 'numapp/print_msg.html', context)


def greeting(request, pk):
    if pk == 1:
        grtMsg = 'おはようございます'
    elif pk == 2:
        grtMsg = 'こんにちは'
    elif pk == 3:
        grtMsg = 'こんばんは'
    context = {
        'greeting' : grtMsg
    }
    return render(request, 'numapp/greeting.html', context)