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
from SCAM.scam.views import LandingView, StudentView, CourseView, PastCourseView, FutureCourseView, ReviewView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LandingView.as_view(), name='landing_page'),
    url(r'^students/(?P<pk>[-\w]+)/$', StudentView.as_view(), name='students'),
    url(r'^students/(?P<pk>[-\w]+)/future_courses/$',
      FutureCourseView.as_view(), name='futurecourses'),
    url(r'^students/(?P<pk>[-\w]+)/past_courses/$', PastCourseView.as_view(),
      name='pastcourses'),
    url(r'^students/(?P<pk>[-\w]+)/current_courses/$', StudentView.as_view(),
      name='currentcourses'),
    url(r'^courses/(?P<pk>[-\w]+)/$', CourseView.as_view(), name='courses'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
