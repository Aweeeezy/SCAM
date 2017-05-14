from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from SCAM.scam.models import Student, Course, Instructor, ActiveCourse, Review, PastCourse, CurrentCourse, FutureCourse, Friend


class LandingView(TemplateView):
  template_name = 'landing.html'

class StudentView(DetailView):
  model = Student
  template_name = 'student.html'

  def get_context_data(self, **kwargs):
    context = super(StudentView, self).get_context_data(**kwargs)
    try:
      context['active_score'] = self.object.days_active/self.object.days_joined*100
    except ZeroDivisionError as e:
      context['active_score'] = 100
    context['past_courses'] = PastCourse.objects.filter(student=self.object)
    context['current_courses'] = CurrentCourse.objects.filter(student=self.object)
    context['future_courses'] = FutureCourse.objects.filter(student=self.object)
    context['friends'] = Friend.objects.filter(user=self.object)
    return context


class CourseView(DetailView):
  model = ActiveCourse
  template_name = 'course.html'

  def get_context_data(self, **kwargs):
    context = super(CourseView, self).get_context_data(**kwargs)
    context['students'] = CurrentCourse.objects.filter(course=self.object)
    return context


class ConnectView(ListView):
  template_name = 'connect.html'

  def get_context_data(self, **kwargs):
    context = super(ConnectView, self).get_context_data(**kwargs)
    # compute similarites
    return context

class ReviewView(ListView):
  model = Review
  template_name = 'review.html'
