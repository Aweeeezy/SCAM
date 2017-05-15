from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from SCAM.scam.models import Student, Course, Instructor, ActiveCourse, Review, PastCourse, CurrentCourse, FutureCourse, Friend


class LandingView(TemplateView):
  template_name = 'landing.html'


class StudentView(DetailView):
  model = Student
  template_name = 'current_courses.html'

  def get_context_data(self, **kwargs):
    context = super(StudentView, self).get_context_data(**kwargs)
    try:
      context['active_score'] = self.object.days_active/self.object.days_joined*100
    except ZeroDivisionError as e:
      context['active_score'] = 100
    context['current_courses'] = CurrentCourse.objects.filter(student=self.object)
    return context


class PastCourseView(DetailView):
  model = Student
  template_name = 'past_courses.html'

  def get_context_data(self, **kwargs):
    context = super(PastCourseView, self).get_context_data(**kwargs)
    try:
      context['active_score'] = self.object.days_active/self.object.days_joined*100
    except ZeroDivisionError as e:
      context['active_score'] = 100
    context['past_courses'] = PastCourse.objects.filter(student=self.object)
    print context['past_courses'].first().instructor
    return context


class FutureCourseView(DetailView):
  model = Student
  template_name = 'future_courses.html'

  def get_context_data(self, **kwargs):
    context = super(FutureCourseView, self).get_context_data(**kwargs)
    try:
      context['active_score'] = self.object.days_active/self.object.days_joined*100
    except ZeroDivisionError as e:
      context['active_score'] = 100
    context['future_courses'] = FutureCourse.objects.filter(student=self.object)
    return context


class FriendView(ListView):
  model = Friend
  template_name = 'friends.html'

  def get_context_data(self, **kwargs):
    context['friends'] = Friend.objects.filter(user=self.object)
    return context


class CourseView(DetailView):
  model = ActiveCourse
  template_name = 'course.html'

  def get_context_data(self, **kwargs):
    context = super(CourseView, self).get_context_data(**kwargs)
    courses = CurrentCourse.objects.filter(course=self.object)
    context['students'] = [course.student for course in courses]
    print kwargs, self.request.user
    for student in context['students']:
      print '??????????', student.id, student.pk
    return context


class ConnectView(ListView):
  template_name = 'connect.html'

  def get_context_data(self, **kwargs):
    context = super(ConnectView, self).get_context_data(**kwargs)
    return context


class ReviewView(ListView):
  model = Review
  template_name = 'review.html'
