#from tastypie.resources import Resource
from polls.models import Student, Attendance, Points, Behavior

from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie_mongoengine import resources
from tastypie_mongoengine import fields


class StudentResource(resources.MongoEngineResource):
    class Meta:
        queryset = Student.objects.all()
        resource_name = 'student'
        authentication = Authentication()
        authorization= Authorization()

class AttendanceResource(resources.MongoEngineResource):
    student = fields.ReferenceField(to='polls.api.StudentResource', attribute='student', full=True)
    class Meta:
        queryset = Attendance.objects.all()
        resource_name = 'attendance'
        authentication = Authentication()
        authorization= Authorization()

class BehaviorResource(resources.MongoEngineResource):
    class Meta:
        queryset = Behavior.objects.all()
        resource_name = 'behavior'
        authentication = Authentication()
        authorization= Authorization()

class PointsResource(resources.MongoEngineResource):
    student = fields.ReferenceField(to='polls.api.StudentResource', attribute='student', full=True)
    behavior = fields.ReferenceField(to='polls.api.BehaviorResource', attribute='behavior', full=True)
    points_date = fields.ReferenceField(to='polls.api.AttendanceResource', attribute='points_date', full=True)
    class Meta:
        queryset = Points.objects.all()
        resource_name = 'points'
        authentication = Authentication()
        authorization= Authorization()
