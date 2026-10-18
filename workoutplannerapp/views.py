from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from .models import User
from django.views.decorators.csrf import csrf_protect
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json
from django.utils import timezone
from .models import *
import random
import string
from decimal import Decimal

def main(request):
    return render(request, 'workoutplannerapp/main.html')

def login(request):
    return render(request, 'workoutplannerapp/login.html')

def logout(request):
    return redirect('main')

@csrf_protect
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.',extra_tags='duplicateemail')
            return render(request, 'workoutplannerapp/login.html')

        existing_count = User.objects.count()
        new_user_id = f'U{existing_count + 1:03}'
        new_user = User(
            user_id=new_user_id,
            user_name=username,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        auth_login(request, new_user)
        return redirect('survey')

    return render(request, 'workoutplannerapp/login.html')

@csrf_protect
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            if(user.user_name == 'admin'):
                return redirect('admin')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.',extra_tags='incorrect')
            return redirect('login')
    return render(request, 'workoutplannerapp/login.html')

@csrf_protect
def survey(request):
    user = request.user
    if request.method == 'POST':
        user.height = request.POST['height']
        user.weight = request.POST['weight']
        user.current_bmi = request.POST['bmi']
        user.sex = request.POST['sex']
        user.save()
        return redirect('home')
    context = {
        'user':user
    }
    return render(request, 'workoutplannerapp/survey.html',context)


def home(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'workoutplannerapp/home.html',context)

def aboutus(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'workoutplannerapp/aboutus.html',context)

def comment(request):
    return render(request, 'workoutplannerapp/comment.html')

def water(request):
    return render(request, 'workoutplannerapp/water.html')

def calorie_calculator(request):
    return render(request, 'workoutplannerapp/calorie-calculator.html')

def profile(request):
    user = request.user
    context = {
        'user':user,
        'amount':user.amount,
        'bmi':user.current_bmi,
        'abs':user.abs,
        'yoga':user.yoga,
        'cardio':user.cardio,
        'upper':user.upper,
        'lower':user.lower,
        'weightgain':user.weightgain,
        'weightloss':user.weightloss
    }
    return render(request, 'workoutplannerapp/profile.html',context)

def diet(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'workoutplannerapp/diet.html',context)

def shop(request):
    return render(request, 'workoutplannerapp/shop.html')

def shop_diet(request):
    return render(request, 'workoutplannerapp/shop_diet.html')

def shop_equipment(request):
    return render(request, 'workoutplannerapp/shop_equipment.html')

def shop_wear(request):
    return render(request, 'workoutplannerapp/shop_wear.html')

def checkout(request):
    return render(request, 'workoutplannerapp/checkout.html')

def exercise(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'workoutplannerapp/exercise.html',context)

def upperbody(request):
    user = request.user
    if request.method == 'POST':
        if(user.upper!=100):
            user.upper += 10
        else:
            user.upper=0
        user.save()
    return render(request, 'workoutplannerapp/upperbody.html')

def upperbody_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.upper!=100):
            user.upper += 10
        else:
            user.upper=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def upperbody_exe(request):
    return render(request, 'workoutplannerapp/upperbody_exe.html')

def lowerbody(request):
    user = request.user
    if request.method == 'POST':
        if(user.lower!=100):
            user.lower += 10
        else:
            user.lower=0
        user.save()
    return render(request, 'workoutplannerapp/lowerbody.html')

def lowerbody_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.lower!=100):
            user.lower += 10
        else:
            user.lower=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def lowerbody_exe(request):
    return render(request, 'workoutplannerapp/lowerbody_exe.html')

def cardio(request):
    user = request.user
    if request.method == 'POST':
        if(user.cardio!=100):
            user.cardio += 10
        else:
            user.cardio=0
        user.save()
    return render(request, 'workoutplannerapp/cardio.html')

def cardio_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.cardio!=100):
            user.cardio += 10
        else:
            user.cardio=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def cardio_exe(request):
    return render(request, 'workoutplannerapp/cardio_exe.html')

def abs(request):
    user = request.user
    if request.method == 'POST':
        if(user.abs !=100):
            user.abs += 10
        else:
            user.abs=0
        user.save()
    return render(request, 'workoutplannerapp/abs.html')

def abs_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.abs !=100):
            user.abs += 10
        else:
            user.abs=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def abs_exe(request):
    return render(request, 'workoutplannerapp/abs_exe.html')

def weightloss(request):
    user = request.user
    if request.method == 'POST':
        if(user.weightloss!=100):
            user.weightloss += 10
        else:
            user.weightloss=0
        user.save()
    return render(request, 'workoutplannerapp/weightloss.html')

def weightloss_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.weightloss!=100):
            user.weightloss += 10
        else:
            user.weightloss=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def weightloss_exe(request):
    return render(request, 'workoutplannerapp/weightloss_exe.html')

def weightgain(request):
    user = request.user
    if request.method == 'POST':
        if(user.weightgain!=100):
            user.weightgain += 10
        else:
            user.weightgain=0
        user.save()
    return render(request, 'workoutplannerapp/weightgain.html')

def weightgain_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.weightgain!=100):
            user.weightgain += 10
        else:
            user.weightgain=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def weightgain_exe(request):
    return render(request, 'workoutplannerapp/weightgain_exe.html')

def yoga(request):
    user = request.user
    if request.method == 'POST':
        if(user.yoga!=100):
            user.yoga += 10
        else:
            user.yoga=0
        user.save()
    return render(request, 'workoutplannerapp/yoga.html')

def yoga_progress(request):
    user = request.user
    if request.method == 'POST':
        if(user.yoga!=100):
            user.yoga += 10
        else:
            user.yoga=0
        user.save()
    return render(request, 'workoutplannerapp/exercise.html')

def yoga_exe(request):
    return render(request, 'workoutplannerapp/yoga_exe.html')

def trainer1(request):
    return render(request, 'workoutplannerapp/trainer1.html')

def trainer2(request):
    return render(request, 'workoutplannerapp/trainer2.html')

def trainer3(request):
    return render(request, 'workoutplannerapp/trainer3.html')

def trainer4(request):
    return render(request, 'workoutplannerapp/trainer4.html')

def trainer5(request):
    return render(request, 'workoutplannerapp/trainer5.html')

def trainer6(request):
    return render(request, 'workoutplannerapp/trainer6.html')


def checkout(request):
    return render(request, 'workoutplannerapp/checkout.html')

def generate_unique_receipt_code():
    return timezone.now().strftime('%Y%m%d%H%M%S') + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def receipt(request):
    user = request.user
    if request.method == 'POST':
        data = request.POST['data']
        amount = request.POST['amount']
        quantity = request.POST['quantity']
        user.address = request.POST['address']
        user.amount += int(amount)
        user.save()
        # Parse the data field from JSON string to Python list of dictionaries
        cart_items = json.loads(data)

        # Generate a unique receipt code
        receipt_code = generate_unique_receipt_code()

        existing_count = Receipt.objects.count()
        receipt = Receipt.objects.create(
            receipt_id = existing_count+1,
            receipt_code=receipt_code,
            total_amount=amount,
            user_id=user.user_id,
            date_of_receipt=timezone.now()
        )

        # Save receipt items data to the database
        for item in cart_items:
            print(item['name'])
            ReceiptItem.objects.create(
                receipt_id=receipt.receipt_id,
                product_name=item['name'],
                quantity=item['quantity'],
                price=item['price']
            )

        # Generate PDF receipt
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="HealthierYou_receipt.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        def draw_header(page_num):
            p.setFont("Helvetica-Bold", 12)
            p.drawString(40, height - 40, "FitXplosion")
            p.drawString(width - 100, height - 40, f"{timezone.now().date()}")

        def draw_footer():
            p.line(40, 50, width - 40, 50)
            p.setFont("Helvetica-Bold", 12)
            p.drawString(40, 35, "Thank you for your purchase!")

        # Draw the header and footer
        draw_header(1)
        draw_footer()

        y = height - 80
        p.drawString(40, y, f"Customer name : {user}")
        y -= 40
        p.drawString(40, y, f"Customer Address : {user.address}")
        y -= 40
        p.setFont("Helvetica", 12)
        for item in cart_items:
            p.drawString(40, y, item['name'])
            p.drawString(300, y, f"{item['price']} Ks")
            p.drawString(400, y, str(item['quantity']))
            p.drawString(480, y, f"{item['total']} Ks")
            y -= 20

        p.line(40, y, width - 40, y)
        y -= 20
        p.setFont("Helvetica-Bold", 12)
        p.drawString(400, y, str(quantity))
        p.drawString(480, y, f"{amount} Ks")
        y -= 20

        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    return render(request, 'workoutplannerapp/checkout.html')


def order(request):
    receipts = Receipt.objects.all()
    
    for receipt in receipts:
        receipt.user_id = User.objects.filter(user_id=receipt.user_id).values_list('user_name', flat=True).first()

    context = {
        'receipts': receipts,
    }
    return render(request, 'workoutplannerapp/admin.html', context)

def order_details(request):
    if request.method == 'POST':
        receipt_id = request.POST['id']
        amount = request.POST['amount']
        total_quantity = 0 
        print(receipt_id)
        items = ReceiptItem.objects.filter(receipt_id = receipt_id).values_list('product_name','price','quantity')
        items_with_totals = []
        for item in items:
            product_name, price, quantity = item
            total_price = price * quantity
            total_quantity += quantity
            items_with_totals.append((product_name, price, quantity, total_price))
        print(items_with_totals)
        for item in items_with_totals:
            print(item[0])
        
        
    context = {
        'amount' : amount,
        'quantity' : total_quantity,
        'items': items_with_totals,
        'receipt_id': receipt_id,
    }
    return render(request, 'workoutplannerapp/order_list.html', context)

def admin_receipt(request):
    user = request.user
    if request.method == 'POST':
        receipt_id = request.POST['id']
        amount = request.POST['amount']
        total_quantity = 0
        print(receipt_id)
        items = ReceiptItem.objects.filter(receipt_id = receipt_id).values_list('product_name','price','quantity')
        items_with_totals = []
        for item in items:
            product_name, price, quantity = item
            total_price = price * quantity
            total_quantity += quantity
            items_with_totals.append((product_name, price, quantity, total_price))


        # Generate PDF receipt
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="HealthierYou_receipt.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        def draw_header(page_num):
            p.setFont("Helvetica-Bold", 12)
            p.drawString(40, height - 40, "FitXplosion")
            p.drawString(width - 100, height - 40, f"{timezone.now().date()}")

        def draw_footer():
            p.line(40, 50, width - 40, 50)
            p.setFont("Helvetica-Bold", 12)
            p.drawString(40, 35, "Thank you for your purchase!")

        # Draw the header and footer
        draw_header(1)
        draw_footer()

        y = height - 80
        p.drawString(40, y, f"Customer name : {user}")
        y -= 40
        p.setFont("Helvetica", 12)
        for item in items_with_totals:
            p.drawString(40, y, item[0])
            p.drawString(300, y, f"{item[1]} Ks")
            p.drawString(400, y, str(item[2]))
            p.drawString(480, y, f"{item[3]} Ks")
            y -= 20

        p.line(40, y, width - 40, y)
        y -= 20
        p.setFont("Helvetica-Bold", 12)
        p.drawString(400, y, str(total_quantity))
        p.drawString(480, y, f"{amount} Ks")
        y -= 20

        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    return render(request, 'workoutplannerapp/checkout.html')