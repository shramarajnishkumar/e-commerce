from email.mime import image
from http import client
from django.shortcuts import redirect,render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import  randrange
from shoesapp import models as s

# from myapp.models import User

# Create your views here.
def aindex(request):
    uid = User.objects.get(email=request.session['email'])
    enq = s.Contact.objects.all()[::-1][0:10]
    review = s.Review.objects.all()[::-1][0:5]
    creview=s.Review.objects.all().count
    pro = product.objects.all().count
    user = User.objects.all().count
    client = s.Register.objects.all().count
    return render(request,'aindex.html',{'uid':uid,'enq':enq,'pro':pro ,'user':user,'rev':review,'crev':creview,'client':client})


def alogin(request):
    try:
        User.objects.get(email=request.session['email'])
        return redirect('aindex')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['email'] = uid.email
                    return redirect('aindex')
                return render(request,'page-login.html',{'msg' : 'incrrect password'})
            except:
                return render(request,'page-register.html',{'msg' : 'email is not register plz register your email'})
        return render(request,'page-login.html')


def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request,'page-register.html',{'msg':'email is already register'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp

                temp = {
                    'name' : request.POST['name'],
                    'email' : request.POST['email'],
                    'password' : request.POST['password'], 
                    'address' : request.POST['address'],
                    'mobile' : request.POST['mobile']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to scarpa shoes'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail(subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp':otp})  
            return render(request,'page-register.html',{'msg':'both password is not same '})
    return render(request,'page-register.html')
def otp(request):

    # if request.method == 'POST':
    #     if request.POST['uotp'] == request.POST['otp']:
    #         global temp
    #         User.objects.create(
    #              name = temp['name'],
    #              email =temp['email'],
    #             password =temp['password']
    #         )
    #         msg = "Account is Created"
    #         return render(request,'page-login.html',{'msg':msg})
    #     return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            User.objects.create(
                name = temp['name'],
                email = temp['email'],
                password = temp['password'],
                address = temp['address'],
                mobile = temp['mobile']
            )
            return render(request,'page-login.html',{'msg' : 'you are sucssesfully register'})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect otp'})
def logout(request):
    del request.session['email']
    return redirect('alogin')

def fpassword(request):
    if request.method == 'POST':
        try:
            uid=User.objects.get(email=request.POST['email'])
            if uid.email == request.POST['email']:
                otp = randrange(1000,9999)
                message = f'Your OTP is {otp}. please enter correctly'
                subject = 'welcome to scarpa'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'fotp.html',{'otp' : otp,'Email':request.POST['email']})
        except:
            return render(request,'page-register.html',{'msg':'email is not register'})
    return render(request,'forgot_password.html')

def fotp(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return redirect('aindex')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if request.POST['password'] == request.POST['otp']:
                    uid.password = request.POST['otp']  #uid.password=9658
                    uid.save()
                    request.session['email'] = uid.email
                    return redirect('aindex')
                return render(request,'fotp.html',{'msg' : 'incorrect password','uid': uid })
            except:
                return render(request,'fotp.html',{'msg' : 'Email is not register '})
        return render(request,'fotp.html')

def profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email= request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        print(request.FILES)
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'app-profile.html',{'uid':uid,'msg':'Profile Updated'})
    return render(request,'app-profile.html',{'uid':uid})

def chpassword(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('aindex')
            return render(request,'change-password.html',{'msg':'Both password are not same'})
        return render(request,'change-password.html',{'msg':'old password is not correct'})
    return render(request,'change-password.html')

def addproduct(request):
    uid = User.objects.get(email=request.session['email'])
    categories = Category.objects.all()
    if request.method == 'POST':
        cate = Category.objects.get(id=request.POST['category'])
        product.objects.create(
            uid = uid,
            category = cate,
            name = request.POST['name'],
            brand = request.POST['brand'],
            price = request.POST['price'],
            image = request.FILES['img'],
            description = request.POST['des'],
        )
        msg = 'product Added'
        return render(request,'add-product.html',{'uid':uid,'categories':categories,'msg':msg})
    return render(request,'add-product.html',{'uid':uid,'categories':categories})
def productadmin(request):
    uid = User.objects.get(email=request.session['email'])
    product_enable = product.objects.filter(active=True)[::-1]
    product_disable = product.objects.filter(active=False)[::-1]
    return render(request,'product-admin.html',{'uid':uid,'product_en':product_enable,'product_dis':product_disable})

def enable(request,xy):
    pro = product.objects.get(id=xy)
    pro.active = True
    pro.save()
    return redirect('productadmin')

def disable(request,xy):
    pro = product.objects.get(id=xy)
    pro.active = False
    pro.save()
    return redirect('productadmin')

def editproduct(request,xy):
    pro = product.objects.get(id=xy)
    cate = Category.objects.all()
    if request.method == 'POST':
        cat = Category.objects.get(id=request.POST['category'])
        pro.name = request.POST['name']
        pro.brand = request.POST['brand']
        pro.price = request.POST['price']
        pro.description = request.POST['des']
        pro.category = cat
        if 'img' in request.FILES:
            pro.image = request.FILES['img']
        pro.save()
        return redirect('productadmin')
    return render(request,'Edit-product.html',{'pro':pro,'cate':cate})

def productdelete(request,xy):
    pro = product.objects.get(id=xy)
    pro.delete()
    return redirect('productadmin')

def usermanage(request):
    uid = User.objects.get(email=request.session['email'])
    user = s.Register.objects.all()
    return render(request,'user-managment.html',{'uid':uid,'user':user})

def userview(request,xy):
    uid = User.objects.get(email=request.session['email'])
    user = s.Register.objects.get(id=xy)
    return render(request,'userview.html',{'uid':uid, 'user':user})

def enquiry(request):
    uid = User.objects.get(email=request.session['email'])
    enquiry = s.Contact.objects.all()
    return render(request,'enquiry.html',{'uid':uid,'enq':enquiry})

def areview(request):
    uid = User.objects.get(email=request.session['email'])
    review=s.Review.objects.all()
    return render(request,'areview.html',{'uid':uid,'rev':review})

    

def index2(request):
    return render(request,'index2.html')
def bootstrap(request):
    return render(request,'table-bootstrap-basic.html')
def calender(request):
    return render(request,'app-calender.html')
def chartist(request):
    return render(request,'chart-chartist.html')
def chartjs(request):
    return render(request,'chart-chartjs.html')
def flot(request):
    return render(request,'chart-flot.html')
def morris(request):
    return render(request,'chart-morris.html')
def peity(request):
    return render(request,'chart-peity.html')
def sparkline(request):
    return render(request,'chart-sparkline.html')
def compose(request):
    return render(request,'email-compose.html')
def inbox(request):
    return render(request,'email-inbox.html')
def read(request):
    return render(request,'email-read.html')
def summernote(request):
    return render(request,'form-editor-summernote.html')
def element(request):
    return render(request,'form-element.html')
def pickers(request):
    return render(request,'form-pickers.html')
def validation(request):
    return render(request,'form-validation-jquery.html')
def wizard(request):
    return render(request,'form-wizard.html')

def layout(request):
    return render(request,'layout-blank.html')
def jqvmap(request):
    return render(request,'map-jqvmap.html')
def error400(request):
    return render(request,'page-error-400.html')
def error403(request):
    return render(request,'page-error-403.html')
def error404(request):
    return render(request,'page-error-404.html')
def error500(request):
    return render(request,'page-error-500.html')
def error503(request):
    return render(request,'page-error-503.html')
def lockscreen(request):
    return render(request,'page-lock-screen.html')

# dsbfs


    