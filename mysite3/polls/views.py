from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from polls.models import Student, Attendance, Behavior, Points
from django.core.urlresolvers import reverse
import mongoengine

from django.views.generic.base import TemplateView
import pdb;

# Create your views here.

def student(request):

    behavior = Behavior.objects.create(
        behavior_id=1,
        behavior_name="Doing_Homework",
    	behavior_points=3,
    )
    behavior = Behavior.objects.create(
        behavior_id=2,
        behavior_name="Disrupting_Class",
    	behavior_points=-2,
    )
	
    behavior = Behavior.objects.create(
        behavior_id=3,
        behavior_name="Helping",
    	behavior_points=5,
    )
	
    points_all = Points.objects.all()
    students_all = Student.objects.all()
    attendance_all = Attendance.objects.all()
    behavior_all = Behavior.objects.all()

    students_info_processed = []
    for student in students_all:
        for attended in attendance_all:
            total_points = 0
            if(len(points_all.filter(student=student, points_date=attended)) > 0):
                points_for_student_on_date = []
                points_for_student_on_date.append(points_all.filter(student=student, points_date=attended))
                for i in range(len(points_for_student_on_date[0])):
                    try:
                        total_points = total_points + points_for_student_on_date[0][i].behavior.behavior_points
                    except:
                        pass
                try:
                    processed_fields = [str(points_for_student_on_date[0][0].student.student_name), points_for_student_on_date[0][0].points_date.attendance_date, total_points]
                    students_info_processed.append(processed_fields)
                    #pdb.set_trace()
                except:
                    pass

    try:
        students_info_sorted_by_date = sorted(students_info_processed, key=lambda studentee: studentee[1])
        for i in range(len(students_info_sorted_by_date)):
            students_info_sorted_by_date[i][1] = str(students_info_sorted_by_date[i][1]).split()[0]
    except:
        students_info_sorted_by_date = students_info_processed

    context = {'students_info_processed': students_info_sorted_by_date}
    #pdb.set_trace()
    return render(request, 'polls/student.html', context)


def input(request):

    behavior = Behavior.objects.create(
        behavior_id=1,
        behavior_name="Doing_Homework",
    	behavior_points=3,
    )
    behavior = Behavior.objects.create(
        behavior_id=2,
        behavior_name="Disrupting_Class",
    	behavior_points=-2,
    )
	
    behavior = Behavior.objects.create(
        behavior_id=3,
        behavior_name="Helping",
    	behavior_points=5,
    )
    return render(request, 'polls/input.html')
