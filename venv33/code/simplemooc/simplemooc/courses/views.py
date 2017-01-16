from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment
from .forms import ContactCourse

# Create your views here.
def index(request):
	courses = Course.objects.all()
	context = {
		'courses': courses
	}
	template_name = 'courses/index.html'
	return render(request, template_name, context)

# def details(request, pk):
# 	course = get_object_or_404(Course,pk=pk)
# 	context = {
# 	  'course': course
# 	  }
# 	template_name = 'courses/details.html'
# 	return render(request, template_name, context)

def details(request, slug):
	course = get_object_or_404(Course,slug=slug)
	context = {}
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()
	context['form'] = form
	context['course'] = course
	template_name = 'courses/details.html'
	return render(request, template_name, context)

#
@login_required
def enrollment(request, slug):
	course = get_object_or_404(Course,slug=slug)
	enrollment, created = Enrollment.objects.get_or_create(user = request.user,
		course=course)

	if created:
		enrollment.active()
		messages.success(request, 'Você foi inscrito com sucesso.')
	else:
		messages.error(request,'Você já está inscrito no curso.' )
	enrollment.save()
	return redirect ('accounts:dashboard')

