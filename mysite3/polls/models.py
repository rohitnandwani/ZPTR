
from django.db import models
from mongoengine import *
import datetime
from django.utils import timezone

# Create your models here.

class Student(Document):
    student_id = IntField(primary_key=True)
    student_name = StringField(max_length=200)
    student_age = IntField()
    student_class = StringField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.student_name
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'

	
class Attendance(Document):
    attendance_id = IntField(primary_key=True)
    student = ReferenceField(Student)
    attendance_date = DateTimeField()
    def __unicode__(self):
        return str(self.attendance_date)

class Behavior(Document):
    behavior_id = IntField(primary_key=True)
    behavior_name = StringField(max_length=200)
    behavior_points = IntField(default=0)
    def __unicode__(self):
        return self.behavior_name


class Points(Document):
    points_id = IntField(primary_key=True)
    student = ReferenceField(Student)
    behavior = ReferenceField(Behavior)
    points_date = ReferenceField(Attendance)
    points = IntField(default=0)
    def __unicode__(self):
        return str(self.points)
    
