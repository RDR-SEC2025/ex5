from django.shortcuts import render
def rectarea(request):
    context={}
    context['p'] = "0"
    context['l'] = "0"
    context['b'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('Intensity','0')
        b = request.POST.get('resistance','0')
        print('request=',request)
        print('Intensity=',l)
        print('resistance=',b)
        p= (int(l)**2) * int(b)
        context['p'] =p
        context['l'] = l
        context['b'] = b
        print('Power=',p)
    return render(request,'mathapp/math.html',context)
