import re
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.http import JsonResponse
from random import randrange
from myapp.models import product as pro
from myapp.models import Category

# Create your views here.
def registration(request):
    if request.method == 'POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'registration.html',{'msg':'Your Email is already registered'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name' : request.POST['name'],
                    'mobile' : request.POST['mobile'],
                    'email' : request.POST['email'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Shoes App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'cotp.html',{'otp':otp})
            return render(request,'registration.html',{'msg':'Both Password Is not Match'})
    return render(request,'registration.html')

def cotp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Register.objects.create(
                name = temp['name'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                password = temp['password']
            )
            msg = "Account is Created"
            return render(request,'login.html',{'msg':msg})
        return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'OTP Is Not Match'})
    # return redirect('registration')
    return render(request,'cotp.html')


def login(request):
    try:
        Register.objects.get(email=request.session['clientemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Register.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['clientemail'] = uid.email
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'registration.html',{'msg':'Email is not registered'})
        return render(request,'login.html')
def clogout(request):
    del request.session['clientemail']
    return redirect('index')

def forgotpass(request):
    if request.method == 'POST':
        try:
            uid=Register.objects.get(email=request.POST['email'])
            if uid.email == request.POST['email']:
                otp = randrange(1000,9999)
                message = f'Your OTP is {otp}. please enter correctly'
                subject = 'welcome to scarpa'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'re-password.html',{'otp' : otp,'Email':request.POST['email']})
        except:
            return render(request,'registration.html',{'msg':'email is not register'})
    return render(request,'forgotpass.html')

def repass(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Register.objects.get(email=request.POST['email'])
                if request.POST['password'] == request.POST['otp']:
                    uid.password = request.POST['otp']  
                    uid.save()
                    request.session['clientemail'] = uid.email
                    return redirect('index')
                return render(request,'re-password.html',{'msg' : 'incorrect password','uid': uid })
            except:
                return render(request,'re-password.html',{'msg' : 'Email is not register '})
        return render(request,'re-password.html')

def index(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count
        return render(request,'index.html',{'uid':uid,'pro':product,'ccart':ccart})
    except:
        return render(request,'index.html',{'pro':product})
    
def allproducts(request):
    product = pro.objects.filter(active=True)
    if request.method == 'POST':
        product= list(pro.objects.filter(name__contains=request.POST['search'],active=True))
        product += list(pro.objects.filter(brand__contains=request.POST['search'],active=True))
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'allproducts.html',{'uid':uid,'pro':product,'ccart':ccart})
    except:
        return render(request,'allproducts.html',{'pro':product})

def cpassword(request):
    uid = Register.objects.get(email=request.session['clientemail'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('index')
            return render(request,'cpassword.html',{'msg':'Both password are not same'})
        return render(request,'cpassword.html',{'msg':'old password is not correct'})
    return render(request,'cpassword.html')

def contact(request):

    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()

        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg,'uid':uid,'ccart':ccart})
        return render(request,'contact.html',{'uid':uid,'ccart':ccart})
    except:
        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg})
        return render(request,'contact.html')
def kid(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'kid.html',{'uid':uid,'pro':product,'ccart':ccart})
    except:
        return render(request,'kid.html',{'pro':product})

def about(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'about.html',{'ccart':ccart})
    except:
        return render(request,'about.html')

def men(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'men.html',{'uid':uid,'pro':product,'ccart':ccart})
    except:
        return render(request,'men.html',{'pro':product})

def women(request):
    product = pro.objects.filter(active=True)
   
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'women.html',{'uid':uid,'pro':product,'ccart':ccart})
    except:
         return render(request,'women.html',{'pro':product})  




def order(request):
    return render(request,'order-complete.html')



def userprofile(request):
    uid = Register.objects.get(email=request.session['clientemail'])
    ccart=Cart.objects.filter(user=uid).count()

    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email= request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        print(request.FILES)
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'userprofile.html',{'uid':uid,'msg':'Profile Updated','ccart':ccart})
    return render(request,'userprofile.html',{'uid':uid,'ccart':ccart})

def product_details(request,pk):
    product = pro.objects.get(id=pk)
    creview=Review.objects.all().count
    review=Review.objects.all()
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        return render(request,'product-detail.html',{'uid':uid,'pro':product,'creview':creview,'review':review,'ccart':ccart})
    except:
        return render(request,'product-detail.html',{'pro':product,'creview':creview,'review':review,'ccart':ccart})

def carts(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        product=pro.objects.get(id=request.POST['id'])
        try:
            cart= Cart.objects.get(user=uid,cart = product) 
            cart.qty += int(request.POST['qty'])
            cart.save() 
        except:
            cart=Cart.objects.create(
                cart=product,
                size=request.POST['size'],
                qty=request.POST['qty'],
                user=uid,
            )            
        return JsonResponse({'msg':'Added To Cart'})
    except:
        return JsonResponse({'msg':'Please Login and try Again'})

def deletecarts(request,pk):
    cart=Cart.objects.get(id=pk)
    cart.delete()
    return redirect('cart')

def review(request,pk):
    product = pro.objects.get(id=pk)
    creview=Review.objects.all().count
    review=Review.objects.all()
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        ccart=Cart.objects.filter(user=uid).count()
        if request.method=='POST':
            Review.objects.create(
                user=uid,
                product=product,
                name=request.POST['name'],
                message=request.POST['review']
            )
            ms='Review is Send'
            return render(request,'review.html',{'uid':uid,'pro':product,'ms':ms,'creview':creview,'review':review,'ccart':ccart})
        return render(request,'review.html',{'uid':uid,'pro':product,'creview':creview,'review':review,'ccart':ccart})
    except:
        return redirect('login')
def cart(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        cart=Cart.objects.filter(user=uid)
        ccart=Cart.objects.filter(user=uid).count()
        car=0
        for i in cart:
            car += (i.cart.price * i.qty)
        dis=car-car*25/100
        return render(request,'cart.html',{'uid':uid,'cart':cart,'car':car,'dis':dis,'ccart':ccart})
    except:
        return redirect('login')
def checkout(request):
    if request.method == 'POST':
        uid = Register.objects.get(email=request.session['clientemail'])
        cart=Cart.objects.filter(user=uid)
        # car=0
        # for i in cart:
        #     car += (i.cart.price * i.qty)
        # dis=car-car*25/100
        # order = Order.objects.create(
        #     cart = cart,
        #     address = request.POST['address'],
        #     pay_mode = request.POST['pay'],
        #     amount = cart.cart.price
        # )
        if request.POST['pay'] == 'Online':
            # currency = 'INR'
            # amount = (product.price)*100  # Rs. 200
        
            # # Create a Razorpay Order
            # razorpay_order = razorpay_client.order.create(dict(amount=amount,
            #                                                 currency=currency,
            #                                                 payment_capture='0'))
        
            # # order id of newly created order.
            # razorpay_order_id = razorpay_order['id']
            # callback_url = f'paymenthandler/{book.id}'
        
            # # we need to pass these details to frontend.
            # context = {}
            # context['razorpay_order_id'] = razorpay_order_id
            # context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            # context['razorpay_amount'] = amount
            # context['currency'] = currency
            # context['callback_url'] = callback_url
            # context['book'] =book
            return render(request,'pay.html')

        else:
            msg = 'Your Booking is confirm you have pay amount onsite.'
            return render(request,'order-complete.html',{'uid':uid,'msg':msg})
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        cart=Cart.objects.filter(user=uid)
        ccart=Cart.objects.filter(user=uid).count()
        car=0
        for i in cart:
            car += (i.cart.price * i.qty)
        dis=car-car*25/100
        return render(request,'checkout.html',{'uid':uid,'cart':cart,'car':car,'dis':dis})
    except:
        return redirect('login')

def order(request):
    # uid = Register.objects.get(email=request.session['clientemail'])
    # cart=Cart.objects.filter(user=uid)
    # order = Order.objects.create(
    #         cart=cart,
    #         address= request.POST['address'],
    #         pay_mode = request.POST['pay'],
    #         amount= cart.cart.price
    #     )
    # if request.POST['pay'] == 'online':
    #     return render(request,'pay.html') 
    # else:
    #     msg = 'your order is confrom'
    return render(request,'order-complete.html')
def add(request):
    return render(request,'add-to-wishlist.html')
