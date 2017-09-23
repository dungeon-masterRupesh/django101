from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe
# Create your views here.
@login_required
def checkout(request):
	if request.method == 'POST':
		stripe.api_key = "sk_test_DFVlrhzszWokbjIsqMplDyiD"

		# Token is created using Stripe.js or Checkout!
		# Get the payment token ID submitted by the form:
		token = request.POST['stripeToken'] # Using Flask

		# Charge the user's card:
		charge = stripe.Charge.create(
		  amount=1000000,
		  currency="usd",
		  description="Example charge",
		  source=token,
		)
	context = {}
	template = 'checkout.html'
	return render(request,template,context)	