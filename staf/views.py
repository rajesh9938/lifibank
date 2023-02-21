from django.shortcuts import render,redirect
from .models import Stafuser,Coustmer,AccountDetails,CreditCardDetails
from django.contrib import messages
from django.core.mail import send_mail
# from pdf_mail import sendpdf
from django.conf import settings
from django.template.loader import render_to_string
from random import shuffle
from staf.helpers import save_pdf

from django.core.mail import EmailMultiAlternatives 
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt

from random import randint
from datetime import date
from dateutil.relativedelta import relativedelta
# Create your views here.
@csrf_exempt
def home(request):
    data = Stafuser.objects.all()
    return render(request, 'index.html',{"data":data})

@csrf_exempt
def about(request):
    return render(request, 'about.html')

@csrf_exempt
def faqs(request):
    return render(request, 'faqs.html')

def single(request):
    return render(request, 'single.html')

@csrf_exempt
def features(request):
    return render(request, 'features.html')

@csrf_exempt
def contact(request):
    return render(request, 'contact.html')



@csrf_exempt
def coustlogin(request):
    if request.method == "POST":
        uname = request.POST["username"]
        upass = request.POST["password"]
        if Stafuser.objects.filter(username=uname,password=upass).exists():
            request.session["username"] = uname
            return redirect('home')
        else:
            return redirect('coustlogin')
    return render(request, 'coustlogin.html')



 
@csrf_exempt                       # staff sgnup to logout.......//////////
def Signup(request):
    if request.method=="POST":
        username = request.POST["username"]
        name = request.POST["name"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]
        user=Stafuser(username=username,name=name,password=password,re_password=re_password)
        if password== re_password:
            user.save()
            messages.success(request, 'successfull created!!')
    return render(request, 'signup.html')

@csrf_exempt
def Login(request):
    if request.method == "POST":
        uname = request.POST["username"]
        upass = request.POST["password"]
        if Stafuser.objects.filter(username=uname,password=upass).exists():
            request.session["username"] = uname
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

@csrf_exempt
def Logout(request):
    del request.session["username"]
    return redirect('login')

@csrf_exempt 
def apply(request):
    if request.method == "POST":
        photo = request.FILES['photo']
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        pin = request.POST["pin"]
        address = request.POST["address"]
        address2 = request.POST["address2"]
        state = request.POST["state"]
        pan_card = request.POST["pan_card"]
        pan_photo = request.FILES["pan_photo"]
        addhar_card = request.POST["addhar_card"]
        adhar_f = request.FILES["adhar_f"]
        adhar_b = request.FILES["adhar_b"]
        cuser = Coustmer(photo=photo,first_name=first_name,last_name=last_name,mobile=mobile,email=email,pin=pin,address=address,address2=address2,state=state,pan_card=pan_card,pan_photo=pan_photo,addhar_card=addhar_card,adhar_f=adhar_f,adhar_b=adhar_b)
        cuser.save()
        messages.success(request, "successfull apply!!")
        return redirect('home')
    return render(request, 'apply.html' )

# apply show pending coustmer

@csrf_exempt
def appled_user(request):
    apply_data = Coustmer.objects.filter(status=False)
    print(apply_data)
    data = Stafuser.objects.all()
    context = {
        "apply_data":apply_data,
        "data":data
    }
    return render(request, 'appled_user.html',context)



@csrf_exempt
def aprove(request,myid):
    set_data = Coustmer.objects.get(id=myid)
    apply_data = Coustmer.objects.all()
    
    data = Stafuser.objects.all()
    context = {
        "set_data":set_data,
        "data":data,
        "apply_data":apply_data
    }  
    return render(request, 'aproved.html',context)

@csrf_exempt
def Reject(request):
    if request.method == "POST":
        set_data = Coustmer.objects.get(id=request.POST['id'])
        email=set_data.email
        subject = "Fi bank"
        message = request.POST['resion']
        msg_template = render_to_string("emailtemp.html",{"message":message})
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list,html_message=msg_template)
        set_data.delete() 
        print("rajesh")  
        return redirect('appled_user')
    
        

# email............
@csrf_exempt
def generate_pdf_sendemail(accountdata,emaildata):
    params = {
        "account_data":accountdata
    }
    res = save_pdf(params)
    file_name = str(res[0])+".pdf"
    print(file_name)
    email = EmailMessage()
    msg_template = render_to_string("emailtemp.html",{"message":emaildata["message"],"header":emaildata["header"]})
    send_file = email.attach_file("public/static/"+file_name)
    subject = emaildata["subject"]
    from_email = settings.EMAIL_HOST_USER
    to = emaildata["email"]
    msg = EmailMultiAlternatives(subject,send_file,from_email,[to])
    msg.attach_alternative(msg_template, "text/html")
    msg.attach_file("public/static/"+file_name)
    msg.send()
    return True

@csrf_exempt
def aproved(request):
    data = Stafuser.objects.all()
    coustmer = Coustmer.objects.get(id=request.POST['email'])
    account_default_number="16711040000"
    acout_last_digiti=["4","3","9","7","5"]
    shuffle(acout_last_digiti)
    account_number=account_default_number+"".join(acout_last_digiti)
    print(account_number,"rajesh")

    coustmer_default_id="865"
    coustmer_last_digiti=["6","3","2","9","7"]
    shuffle(coustmer_last_digiti)
    coustmer_number=coustmer_default_id+"".join(coustmer_last_digiti)
    print(coustmer_number)

    ac_no = account_number
    c_id = coustmer_number
    Coustmer.objects.filter(id=request.POST['email']).update(status=True)
    coustmer_accountDetails = AccountDetails(account_no=ac_no,coustmerid=c_id,coustmer=coustmer)
    coustmer_accountDetails.save()

    account_data = AccountDetails.objects.get(account_no=ac_no)
    email_data = {
        "header":"account creation",
        "message":"successfully account created, please find the account diteale bellow pdf",
        "subject":"new account opening",
        "email":coustmer.email

    }
    
    generate_pdf_sendemail(account_data,email_data)
    redirect('appled_user')

    return render(request, 'aproved.html',{"data":data})

# //send passbook...............................
@csrf_exempt
def aproved_user(request):
    aproved_data = AccountDetails.objects.filter(status=False)
    data = Stafuser.objects.all()
    context = {
        "aproved_data":aproved_data,
        "data":data
    }

    return render(request, 'aproved_user.html',context)

@csrf_exempt
def account_book(request,myid):
    prover_data = AccountDetails.objects.get(id=myid)
    aproved_data = AccountDetails.objects.all()
    
    context = {
        "prover_data":prover_data,
        "aproved_data":aproved_data,
    } 
    return render(request, 'account_book.html',context)


@csrf_exempt
def gen_pdf(request,myid):
    account_data = AccountDetails.objects.get(id=myid)
    params = {
        "account_data":account_data
    }
    res = save_pdf(params)
    file_name = str(res[0])+".pdf"
    print(file_name)
    email = EmailMessage()
    send_file = email.attach_file("public/static/"+file_name)
    subject = "passbook"
    from_email = settings.EMAIL_HOST_USER
    to = "tt9080498@gmail.com"
    msg = EmailMultiAlternatives(subject,send_file,from_email,[to])
    msg.attach_file("public/static/"+file_name)
    msg.send()
    return redirect('aproved_user')
                        # coustmer apply to aproved........\\\\\\\\\\\
@csrf_exempt
def forget(request):
    if request.method=="POST":
        email=request.POST['email']
        subject = "Fi bank"
        message = "8746"
        header = "OTP"
        msg_template = render_to_string("emailtemp.html",{"message":message,"header":header})
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list,html_message=msg_template)
    return render(request, 'forget.html')

@csrf_exempt
def apply_credit_card(request):
    appled_creditcard = AccountDetails.objects.filter(creditCard="apply")
    data = Stafuser.objects.all()
    context = {
        "appled_creditcard":appled_creditcard,
        "data":data
    }
    return render(request, 'apply_credit_card.html',context)

@csrf_exempt
def applyed_credit_card(request,myid):
    set_data = AccountDetails.objects.get(id=myid)
    data = Stafuser.objects.all()
    context = {
        "set_data":set_data,
        "data":data
    }
    return render(request, 'applyed_credit_card.html',context)
    
@csrf_exempt
def aproved_credit_card(request):
    coustmer_no = AccountDetails.objects.get(id=request.POST['account_no'])
    
    digit1 = ["1","2","3","4","5","6","7","8","9","0","0","5"]
    shuffle(digit1)
    credit_card_no = "5453"+"".join(digit1)
    print(credit_card_no,"credit_card_no")

    def random_with_N_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
    res = random_with_N_digits(3)
    cvv = res
    print(cvv,"cvv")

    new_date = date.today() + relativedelta(years=5)
    ex_date = str(new_date)
    print('new date is : ' + ex_date)
    ccard = CreditCardDetails(credit_card_no=credit_card_no,cvv=cvv,ex_date=ex_date,coustmer1=coustmer_no)
    ccard.save()

    acupdate =AccountDetails.objects.filter(id=request.POST['account_no']).update(creditCard="success")
    print(acupdate,"********")

    messages.success(request, "successfull create!!")
    return redirect('apply_credit_card')
    
    return render(request, 'aproved_credit_card.html')

# sgvdghsvghd