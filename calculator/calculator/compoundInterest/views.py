from django.shortcuts import render

# Create your views here.


def calculate(request):
    if request.method == 'POST':
        principal = float(request.POST.get('principal'))
        time = float(request.POST.get('time'))
        interest = float(request.POST.get('interest'))

        # Calculate the compound interest
        result = principal * (1 + (interest/100)) ** time

        context = {
            'result': result
        }

  

        return render(request, 'cal.html',{'result':result})

    return render(request, 'cal.html')


