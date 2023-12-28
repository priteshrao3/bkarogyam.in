from django.shortcuts import render, redirect
import requests
from django.contrib import auth
from .forms import CarrerForm, docforms
from django.contrib import messages
from .models import Contact, Career, Gallery, Login, DoctorUser, Employee_Slider, Doctor_Slider, Employee_Document, Doctor_Document, Products, Category, Testimonial, User_Document, User_Order, Product_Order

# blog_api = requests.get('https://bkarogyam.com/erp-api/post/').json()
# video_api = requests.get('https://bkarogyam.com/erp-api/video/').json()
# events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
# job_api = requests.get('https://bkarogyam.com/erp-api/dynamic-data/?category=Career&sub_category=Openings&page_size=50').json()
#tesing app user 
from django.http import JsonResponse

def testing(request):
    data = Products.Objects.all()
    return JsonResponse({'data':data},safe = False)
#end testing user

# Create views here.
def index(request):
    slider_api = requests.get('https://bkarogyam.com/erp-api/slider/').json()
    blog_api = requests.get('https://bkarogyam.com/erp-api/post/').json()
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    gallery = Gallery.objects.all()
    testimonial = Testimonial.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('index')
    else:
        return render(request, 'index.html', {'slider': slider_api, 'testimonial':testimonial,'gallery':gallery [0:5],'blogs': blog_api['results'][0:5], 'events': events_api['results'][0:5]})


def about(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('about')
    else:
        return render(request, 'aboutus.html', {'events': events_api['results'][0:5]})


def events(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('events')
    else:
        return render(request, 'event.html', {'events': events_api['results']})


def events_detail(request, e_id):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('events_detail')
    else:
        return render(request, 'events_details.html', {'e_id': e_id, 'events': events_api['results']})


def blogs(request):
    blog_api = requests.get('https://bkarogyam.com/erp-api/post/').json()
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('blogs')
    else:
        return render(request, 'blogs.html', {'blogs': blog_api['results'], 'events': events_api['results'][0:5]})


def blogs_details(request, b_id):
    blog_api = requests.get('https://bkarogyam.com/erp-api/post/').json()
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('blogs_details')
    else:
        return render(request, 'blogs_details.html', {'b_id': b_id, 'blogs': blog_api['results'], 'events': events_api['results'][0:5]})


def gallery(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    gallery = Gallery.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('gallery')
    else:
        return render(request, 'gallery.html', {'events': events_api['results'][0:5],'gallery':gallery,})


def career(request):
    job_api = requests.get(
        'https://bkarogyam.com/erp-api/dynamic-data/?category=Career&sub_category=Openings&page_size=50').json()
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        files = request.FILES
        img = files.get('img', None)
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        applyfor = request.POST.get('applyfor')
        career = Career(name=name, mobileno=mobileno, email=email, address=address,
                        qualification=qualification, applyfor=applyfor, img=img)
        career.save()
        return redirect('career')
        # form = CarrerForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
    else:
        # form = CarrerForm()
        return render(request, 'career.html', {'job': job_api['results'], 'events': events_api['results'][0:5]})


def videos(request):
    video_api = requests.get('https://bkarogyam.com/erp-api/video/').json()
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('videos')
    else:
        return render(request, 'videos.html', {'video': video_api['results'], 'events': events_api['results'][0:5]})


def contactus(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('contact')
    else:
        return render(request, "contact.html", {'events': events_api['results'][0:5]})


def download(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    user_doc = User_Document.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('download')
    else:
        return render(request, 'download.html', {'user_doc': user_doc, 'events': events_api['results'][0:5]})


def diseases(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('diseases')
    else:
        return render(request, 'diseases.html', {'events': events_api['results'][0:5]})


def product(request):
    return render(request, 'diseases.html')
    # return redirect("http://shop.arogyambharat.com/")


def allopath_ayurveda(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    allopath_medicine_api = requests.get(
        'https://bkarogyam.com/erp-api/conversion/').json()
    allopath_medicine_name = requests.get(
        'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Allopath').json()
        
    product_name = request.GET.get('product_name')
    if product_name:
            allopath_medicine_api = requests.get(
                'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Allopath&id='+product_name).json()

    
    ayurveda_medicine_api = requests.get(
        'https://bkarogyam.com/erp-api/conversion/').json()
    ayurveda_medicine = requests.get(
        'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Ayurveda').json()
    
    ayurveda_name = request.GET.get('ayurveda_name')
    if ayurveda_name:
            ayurveda_medicine_api = requests.get(
                'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Ayurveda&id='+ayurveda_name).json()



    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('allopath_ayurveda')
    else:
        return render(request, 'allopath_to_ayurveda.html', {'events': events_api['results'][0:5], 'allopath_ayurveda': allopath_medicine_api['results'], 'ayurveda_medicine': ayurveda_medicine_api['results'], 'allopath_name':allopath_medicine_name ['results'], 'ayurveda_medicine_name':ayurveda_medicine ['results']})


def ayurveda_allopath(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    allopath_medicine_api = requests.get(
        'https://bkarogyam.com/erp-api/conversion/').json()
    allopath_medicine_name = requests.get(
        'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Allopath').json()
        
    product_name = request.GET.get('product_name')
    if product_name:
            allopath_medicine_api = requests.get(
                'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Allopath&id='+product_name).json()

  
    ayurveda_medicine_api = requests.get(
        'https://bkarogyam.com/erp-api/conversion/').json()
    ayurveda_medicine = requests.get(
        'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Ayurveda').json()
    
    ayurveda_name = request.GET.get('ayurveda_name')
    if ayurveda_name:
            ayurveda_medicine_api = requests.get(
                'https://bkarogyam.com/erp-api/conversion/medicines/?medicine_type=Ayurveda&id='+ayurveda_name).json()



    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('allopath_ayurveda')
    else:
        return render(request, 'ayurveda_to_allopath.html', {'events': events_api['results'][0:5], 'allopath_ayurveda': allopath_medicine_api['results'], 'ayurveda_medicine': ayurveda_medicine_api['results'], 'allopath_name':allopath_medicine_name ['results'], 'ayurveda_medicine_name':ayurveda_medicine ['results']})


# ------------------- Doctor -------------------
def doctor_login(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    if request.method == 'POST':
        docuser = request.POST['user']
        docpass = request.POST['password']
        doctor = auth.authenticate(username=docuser, password=docpass)
        # Not Success
        # print(doctor.user_type)
        if doctor is None:
            return redirect('doctor_login')
        # Success
        elif doctor.user_type == DoctorUser.DOCTOR:
            auth.login(request, doctor)
            return redirect('doctor_diseases')
        elif doctor.user_type == DoctorUser.EMPLOYEE:
            auth.login(request, doctor)
            return redirect('employee_login')
    else:
        return render(request, 'doc_login.html', {'events': events_api['results'][0:5]})


def doctor_profile(request, id):

    if request.method == 'POST':
        doc = DoctorUser.objects.get(pk=id)
        doctor_data = docforms(request.POST, request.FILES,instance=doc)
        if doctor_data.is_valid():
            doctor_data.save()
        print(doctor_data)
        return redirect('doctor_diseases')

    else:
        return render(request, 'doc_diseases.html')


def doctor_diseases(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    # doctor_slider_api = requests.get('https://bkarogyam.com/erp-api/landing_page_content/').json()
    doctor_slider = Doctor_Slider.objects.all()
    doctor_document = Doctor_Document.objects.all()
    category = Category.objects.all()
    product = Products.objects.all()
    doctor_info = DoctorUser.objects.all()
    doctor_info = DoctorUser.objects.filter(id=request.user.pk).first()
    # print(doctor_info)

    product_category = request.GET.get('product_category')
    if product_category:
        product = product.filter(product_cat=product_category)

    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('doctor_diseases')

    if request.method == "POST":
        po_doctor_name = request.POST.get('po_doctor_name')
        po_phoneno = request.POST.get('po_phoneno')
        po_doc_messages = request.POST.get('po_doc_messages')
        po_product = request.POST.getlist('po_product[]')
        # print(po_product)
        products = []
        for item in po_product:
            product_item = Products.objects.get(id=item)
            po_qty = request.POST.get('po_qty'+item)
            products.append(Product_Order.objects.create(
                product=product_item, qty=po_qty))
        doctor_data = User_Order.objects.create(
            doctor_name=po_doctor_name, phoneno=po_phoneno, doc_messages=po_doc_messages)
        doctor_data.products.set(products)
        doctor_data.save()
        return redirect('doctor_diseases')
    else:
        return render(request, 'doc_diseases.html', {'product': product, 'doctor_info': doctor_info, 'category': category, 'doctor_slider': doctor_slider, 'doctor_doc': doctor_document, 'events': events_api['results'][0:5]})


# ------------------- Employee -------------------


def employee_login(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()

    if request.method == 'POST':
        docuser = request.POST['user']
        docpass = request.POST['password']
        doctor = auth.authenticate(username=docuser, password=docpass)
        # Not Success
        # print(doctor.user_type)
        if doctor is None:
            return redirect('employee_login')
        # Success
        elif doctor.user_type == DoctorUser.DOCTOR:
            auth.login(request, doctor)
            return redirect('doctor_diseases')
        elif doctor.user_type == DoctorUser.EMPLOYEE:
            auth.login(request, doctor)
            return redirect('employee_dashboard')
    else:
        return render(request, 'employee_login.html', {'events': events_api['results'][0:5]})


def employee_dashboard(request):
    events_api = requests.get('https://bkarogyam.com/erp-api/events/').json()
    # arogyam_slider_api = requests.get('https://bkarogyam.com/erp-api/arogyam_slider/').json()
    slider = Employee_Slider.objects.all()
    document = Employee_Document.objects.all()
    employee_info = DoctorUser.objects.all()
    employee_info = DoctorUser.objects.filter(id=request.user.pk).first()
    get_user = request.user
    # print(get_user)
    if request.method == "POST":
        name = request.POST.get('name')
        mobileno = request.POST.get('mobileno')
        email = request.POST.get('email')
        messages = request.POST.get('messages')
        subject = request.POST.get('subject')
        contact = Contact(name=name, mobileno=mobileno,
                          email=email, messages=messages, subject=subject)
        contact.save()
        return redirect('employee_dashboard')
    else:
        return render(request, 'employee_dashboard.html', {'get_user':get_user, 'events': events_api['results'][0:5], 'employee_info':employee_info, 'slider': slider, 'document': document})
