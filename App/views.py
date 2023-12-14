from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import Atm


# Create your views here.
def home(request):
    if 'user' in request.session:
        current_user = request.session['user']

        return render(request, 'home.html', {'current_user': current_user})
    else:
        return redirect('/login/')

    return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cardno = request.POST.get('card_no')
        pin = request.POST.get('pin')
        amount =request.POST.get('amount')

        if Atm.objects.filter(Card_Number=cardno, Pin=pin).count() > 0:
            return HttpResponse('Card-number or pin already exists.')
        else:
            user = Atm(Name=name, Card_Number=cardno, Pin=pin, Balance=amount)
            user.save()

            return redirect("/login/")
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        cardno = request.POST.get('card_no')
        pin = request.POST.get('pin')
        check_user = Atm.objects.filter(Card_Number=cardno, Pin=pin)
        if check_user:
            request.session['user'] = cardno
            print('fghjk')
            return redirect('/profile/')
        else:
            return HttpResponse('Please enter valid Card-number or Pin.')

    return render(request, "login.html")


def profile(request):
    if 'user' in request.session:
        current_user = request.session['user']
        pro= Atm.objects.filter(Card_Number=current_user)

        return render(request, 'profile.html', {'current_user': current_user, 'profile':pro})

def deposit(request,id):
    ins = Atm.objects.get(id=id)
    if request.method == "POST":


        amt = request.POST.get('amount')
        ins.Balance += int(amt)

        ins.save()
        return redirect('/profile/')

    return render(request, 'deposit.html',{'ins':ins})


def withdraw(request,id):

    ins = Atm.objects.get(id=id)




    if request.method == "POST":
        withdrawal_amount = request.POST.get('amount')



        if withdrawal_amount == 0:
            return HttpResponse("Withdrawal amount must be greater than zero")

        if int(withdrawal_amount) > int(ins.Balance):
            return HttpResponse("Insufficient funds")

        ins.Balance -= int(withdrawal_amount)
        ins.save()
        return redirect('/profile/')

    return render(request, 'withdraw.html', { 'ins': ins})


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/login/')
    return redirect('/login/')
