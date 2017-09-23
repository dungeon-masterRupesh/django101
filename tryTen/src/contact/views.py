from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	confirm_message = None
	if form.is_valid():
		print("HI")
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comments'] 
		subject = 'MESSSAGE FORM ME'
		message = '%s  %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		print(subject, message, emailFrom, emailTo)
		#send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
		title = 'Thanks'
		confirm_message = 'see you soon'
		form = None
	template = 'contact.html'
	context = {'title': title, 'form': form,'confirm_message': confirm_message,}
	return render(request,template,context)

