from django.shortcuts import render,redirect
from staf.models import Coustmer,AccountDetails,CoustmerOtp,CreditCardDetails
from coustuser.models import Transactions
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from random import shuffle
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def coustmer_signup(request):
    if request.method=="POST":
        ac_no = request.POST['account_no']
        coustid = request.POST['coustmerid']
        accountdetail = AccountDetails.objects.filter(account_no = ac_no,coustmerid = coustid)
        if accountdetail.exists():
            accountdetail = accountdetail[0]
            # print(accountdetail.coustmer,"********************8")
            coustmer = Coustmer.objects.get(id=accountdetail.coustmer_id)
            
            a = ["1","9","2","4"]
            shuffle(a)
            res ="".join(a)
            subject = "Fi bank"
            header = "OTP"
            message = res
            msg_template = render_to_string("emailtemp.html",{"message":message,"header":header})
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [coustmer.email]
            send_mail(subject, message, from_email, recipient_list,html_message=msg_template)
            # coustmer=Coustmer.objects.get(email=email)
            saveotp = CoustmerOtp(otp=message,coustmer=coustmer)
            saveotp.save()
            return render(request, 'coustmer_temp/verify.html',{"coustmer":coustmer})   
    return render(request, 'coustmer_temp/signup.html')
@csrf_exempt
def verify_otp(request):
    if request.method=="POST":
        coustmer = Coustmer.objects.get(email=request.POST['email'])
        otp = request.POST['otp']
        mpin = request.POST['mpin']
        mpin2 = request.POST['mpin2']
        if mpin == mpin2:
            coustmerotp = CoustmerOtp.objects.filter(otp=otp,coustmer=coustmer)
            if coustmerotp.exists():
                coustmerotp.delete()
                AccountDetails.objects.filter(coustmer=coustmer).update(mpin=mpin)
                return redirect("coustmer_login")

    return render(request, 'coustmer_temp/verify.html')
@csrf_exempt
def coustmer_home(request):
    # accountdetail = AccountDetails.objects.filter(coustmerid = coustid,mpin=mpin)
    # if accountdetail.exists():
    coustid = request.session["coustmerid"]
    accountdetail = AccountDetails.objects.filter(coustmerid = coustid)
    accountdetail = accountdetail[0]
    # print(accountdetail.coustmer,"********************8")
    coustmer = Coustmer.objects.get(id=accountdetail.coustmer_id)
    data = coustmer.first_name
    return render(request, 'coustmer_temp/coustmer_home.html',{"data":data})
@csrf_exempt
def coustmer_login(request):
    if request.method=="POST":
        coustid = request.POST['coustmerid']
        mpin = request.POST['mpin']
        accountdetail = AccountDetails.objects.filter(coustmerid = coustid,mpin=mpin)
        if accountdetail.exists():
            request.session["coustmerid"] = coustid
            return redirect('coustmer_home')
        else:
            return redirect('coustmer_login')
    return render(request, 'coustmer_temp/login.html')
@csrf_exempt
def coustmer_logout(request):
    del request.session["coustmerid"]
    return redirect('coustmer_login')

@csrf_exempt                # coustmer coustmer_dashboard /coustmer_withdraw / coustmer_confirmwithdraw
def coustmer_dashboard(request):
    accountdetail = AccountDetails.objects.filter(coustmerid = request.session["coustmerid"])
    accountdetail = accountdetail[0]
    coustmer = Coustmer.objects.get(id=accountdetail.coustmer_id)
    # print(coustmer.address,"**********10")
    name = coustmer.first_name+" "+coustmer.last_name
    coustmer_detail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"])
    context = {
        "coustmer_detail":coustmer_detail,
        "coustmer":coustmer,
        "name":name,
    }
    # print(coustmer_detail.balance)
    return render(request, 'coustmer_temp/profile.html',context)


@csrf_exempt
def coustmer_withdraw(request):
    accountdetail = AccountDetails.objects.filter(coustmerid = request.session["coustmerid"])
    accountdetail = accountdetail[0]
    coustmer_detail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"])
    context = {
        "coustmer_detail":coustmer_detail,
    }
    if request.method == "POST":
        print(request.POST,"********")
        withdraw_no = request.POST["withdraw_no"]
        ifsc = request.POST["ifsc"]
        amount = request.POST["amount"]
        m__pin = request.POST["m__pin"]
        if coustmer_detail.mpin == m__pin:
            available = coustmer_detail.balance-float(amount)

            coustmer_detail = AccountDetails.objects.filter(coustmerid = request.session["coustmerid"]).update(balance=available)

            transaction_no = ["4","3","9","7","5","1","2","8"]
            shuffle(transaction_no)
            transaction_number ="".join(transaction_no)
            transaction_type = "debid"
            transaction_accountDetails = Transactions(transaction_no=transaction_number,withdraw_no=withdraw_no,amount=amount,account=accountdetail,transaction_type=transaction_type)
            transaction_accountDetails.save()
            return redirect('coustmer_success')

    return render(request, 'coustmer_temp/withdraw.html',context)


@csrf_exempt
def coustmer_success(request):

        return render(request, 'coustmer_temp/coustmer_success.html')
@csrf_exempt
def coustmer_transaction(request):
    coustmer_detail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"])
    accountdetail = AccountDetails.objects.filter(coustmerid = request.session["coustmerid"])
    accountdetail = accountdetail[0]
    coustmer = Coustmer.objects.filter(id=accountdetail.coustmer_id)
    transactions_data = Transactions.objects.filter(account__coustmerid=request.session["coustmerid"])
    context = {
            "transactions_data":transactions_data,
            "coustmer_detail":coustmer_detail
            }
    return render(request, 'coustmer_temp/transaction.html',context)


# creadit card//////////////////
@csrf_exempt
def credit_card(request):
    return render(request, 'coustmer_temp/apply1_creaditcard.html')
@csrf_exempt
def apply1_credit_card(request):
    if request.method == "POST":
        accountdetail = AccountDetails.objects.filter(coustmerid = request.session["coustmerid"]).update(creditCard = "apply")
        print("ravgdvgh")
        return redirect('coustmer_dashboard')

@csrf_exempt
def creadit_card(request):
    accountdetail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"])
    res = CreditCardDetails.objects.get(coustmer1=accountdetail)
    print(res.coustmer1.coustmer.first_name)
    name = res.coustmer1.coustmer.first_name+" "+res.coustmer1.coustmer.last_name

    no = res.credit_card_no
    d = str(no)
    result = ""
    ccno=""
    for i in range(len(d)):
        result = result + d[i]
        if len(result)==4:
            ccno =ccno+ result+" "
            print(ccno)
            result=""

    context={
        "credit_data":res,
        "name":name,
        "ccno":ccno
    }
    return render(request, 'coustmer_temp/creaditcard.html',context)

@csrf_exempt
def cardwithdraw(request):
    accountdetail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"])
    c_detail = CreditCardDetails.objects.get(coustmer1=accountdetail)
    if request.method == "POST":
        name_on_Card = request.POST['cardname']
        credit_card_num = request.POST['cardnumber']
        exp_date = request.POST['expyear']
        cvv = request.POST['cvv']
        ammount = request.POST['money']
        if c_detail.credit_card_no == credit_card_num and c_detail.cvv==cvv:
            ac_money = accountdetail.balance-ammount
            accountdetail = AccountDetails.objects.get(coustmerid = request.session["coustmerid"]).update(balance=ac_money)
            


    return render(request, 'coustmer_temp/cardwithdraw.html')