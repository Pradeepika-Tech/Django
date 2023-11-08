from django.views.generic import ListView
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    