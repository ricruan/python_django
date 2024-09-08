from django.shortcuts import render

from mytest.models import Student


# Create your views here.

def index(request):
    student_list = Student.objects.order_by("-student_name")[:5]
    context = {
        "student_list": student_list,
    }
    return render(request, "student/index.html", context)