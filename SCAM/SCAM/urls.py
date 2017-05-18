"""SCAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from SCAM.scam.views import LandingView, StudentView, CourseView, PastCourseView, FutureCourseView, ReviewView, SignUpView, ProfileRedirectView, InstructorView, FriendView, ConnectView, ReportView, ConnectResultsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/profile/', ProfileRedirectView.as_view()),
    url(r'^$', auth_views.login, {'template_name': 'landing.html'},
        name='landing_page'),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^students/(?P<pk>[-\w]+)/$', StudentView.as_view(), name='students'),
    url(r'^students/(?P<pk>[-\w]+)/future_courses/$',
      FutureCourseView.as_view(), name='futurecourses'),
    url(r'^students/(?P<pk>[-\w]+)/past_courses/$', PastCourseView.as_view(),
      name='pastcourses'),
    url(r'^students/(?P<pk>[-\w]+)/current_courses/$', StudentView.as_view(),
      name='currentcourses'),
    url(r'^students/(?P<pk>[-\w]+)/friends/$', FriendView.as_view(), name='friends'),
    url(r'^courses/(?P<pk>[-\w]+)/$', CourseView.as_view(), name='courses'),
    url(r'^instructors/(?P<pk>[-\w]+)/$', InstructorView.as_view(),
        name='instructors'),
    url(r'^connect/(?P<pk>[-\w]+)/$', ConnectView.as_view(), name='connect'),
    url(r'^connect/(?P<pk>[-\w]+)/results/$', ConnectResultsView.as_view(),
        name='connectresults'),
    url(r'^reviews/$', ReviewView.as_view(), name='reviews'),
    url(r'^reporting/$', ReportView.as_view(), name='reporting'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
