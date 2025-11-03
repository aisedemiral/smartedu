from django.shortcuts import render
from . models import Course

def course_list(request):
    course=Course.objects.all().order_by('-date')

    context = {
        'courses': course
    }

    return render(request, 'courses.html',context)

 