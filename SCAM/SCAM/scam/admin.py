from django.contrib import admin
from SCAM.scam.models import Student, Course, ActiveCourse, Instructor, Review, PastCourse, CurrentCourse, FutureCourse, Friend


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['sid', 'name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['name']


@admin.register(ActiveCourse)
class ActiveCourseAdmin(admin.ModelAdmin):
  list_display = ['name', 'instructor']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
  list_display = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ['student', 'course', 'instructor', 'rating']


@admin.register(PastCourse)
class PastCourseAdmin(admin.ModelAdmin):
  list_display = ['student', 'course']


@admin.register(CurrentCourse)
class CurrentCourseAdmin(admin.ModelAdmin):
  list_display = ['student', 'course']


@admin.register(FutureCourse)
class FutureCourseAdmin(admin.ModelAdmin):
  list_display = ['student', 'course']


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
  list_display = ['user', 'friend']
