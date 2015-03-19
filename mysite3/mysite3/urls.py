from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from polls.api import StudentResource, AttendanceResource, PointsResource, BehaviorResource

from polls import views

v1_api = Api(api_name='v1')
v1_api.register(StudentResource())
v1_api.register(AttendanceResource())
v1_api.register(PointsResource())
v1_api.register(BehaviorResource())

urlpatterns = patterns('',
    url(r'^student/', views.student),
    url(r'^input/', views.input),
    url(r'^api/', include(v1_api.urls)),
)
