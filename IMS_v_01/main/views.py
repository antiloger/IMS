from django.apps import apps
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Teacher, Course, TeacherEnroll, StudentEnroll, Payment, Attendance, Salary
from .forms import Studentform

tableArray_ub = ['Student', 'Teacher', 'Course']
tableArray_eb = ['Student', 'Teacher',]
# Create your views here.
def index(request, model_name):

    try:
        model_o = apps.get_model(app_label='main', model_name=model_name)
        std_detail = model_o.objects.all().values()
        f_det = model_o._meta.fields
        stdDet = list(std_detail.values())
        flist = [list(i.values()) for i in stdDet]

    except Student.DoesNotExist:
        raise Http404("data not valid")

    return render(request, 'main/tables.html', {'std_det': flist, 'f_det': f_det, 'table_name':model_name})


def add(request):
    if request.method == "POST":
        form = Studentform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Student add successfully!!!'))
        return render(request, 'main/AUR.html', {})

    else:
        return render(request, 'main/AUR.html', {})


def update(request, model_name, std_ID):
    previous_page = request.META.get('HTTP_REFERER')
    model_o = apps.get_model(app_label='main',model_name=model_name)
    up_obj = model_o.objects.get(pk=std_ID)
    enroll_detail = Course.objects.filter(student=std_ID).values("course_name")
    payment_detail = Payment.objects.filter(std_ID=std_ID)
    print(payment_detail)

    #update btn
    form = Studentform(request.POST or None, instance=up_obj)
    if 'UpdateStd' in request.POST:
        if form.is_valid():
            form.save()
            return redirect(previous_page)
    print(up_obj)
    return render(request, 'main/update_form/std_update.html', {'up_obj': up_obj, 'model_o': model_o, 'enroll_det':enroll_detail,'pay_det':payment_detail})

