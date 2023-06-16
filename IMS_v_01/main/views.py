from django.apps import apps
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Teacher, Course, TeacherEnroll, StudentEnroll, Payment, Attendance, Salary
from .forms import Studentform, Teacherform

tableArray_ub = ['Student', 'Teacher', 'Course','student', 'teacher','course']
tableArray_eb = ['Student', 'Teacher','student', 'teacher']


# Create your views here.
def index(request, model_name):

    try:
        model_o = apps.get_model(app_label='main', model_name=model_name)
        std_detail = model_o.objects.all().values()
        f_det = model_o._meta.fields
        stdDet = list(std_detail.values())
        flist = [list(i.values()) for i in stdDet]
        print(model_o)

    except Student.DoesNotExist:
        raise Http404("data not valid")

    return render(request, 'main/tables.html', {'model_o':model_o, 'std_det': flist, 'f_det': f_det, 'table_name':model_name, 'tableArray_eb':tableArray_eb, 'tableArray_ub':tableArray_ub})


def add(request):
    if request.method == "POST":
        form = Studentform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Student add successfully!!!'))
        return render(request, 'main/AUR.html', {})

    else:
        return render(request, 'main/AUR.html', {})


# Update btn in tables
def update(request, model_name, model_ID):
    previous_page = request.META.get('HTTP_REFERER')
    model_obj = apps.get_model(app_label='main' , model_name=model_name)
    up_obj = model_obj.objects.get(pk=model_ID)

    m_strname = model_name.lower()

    if m_strname == "student":

        enroll_detail = Course.objects.filter(student=model_ID).values("course_name")
        payment_detail = Payment.objects.filter(std_ID=model_ID)

        form = Studentform(request.POST or None, instance=up_obj)

        if 'UpdateStd' in request.POST:
            if form.is_valid():
                form.save()
                return redirect(previous_page)

        return render(request, 'main/update_form/std_update.html',
                      {'up_obj': up_obj, 'enroll_det': enroll_detail, 'pay_det': payment_detail, 'model_ID': model_ID})

    if m_strname == "teacher":

        form = Teacherform(request.POST or None, instance=up_obj)

        if 'UpdateTeach' in request.POST:
            if form.is_valid():
                form.save()
                return redirect(previous_page)

        return render(request, 'main/update_form/teacher_update.html',
                      {'up_obj': up_obj, 'model_ID': model_ID})


def delete(request, model_name, model_ID):
    model_o = apps.get_model(app_label='main', model_name=model_name)
    obj_del = model_o.objects.get(pk=model_ID)
    obj_del.delete()
    return redirect('index', model_name=model_name)
