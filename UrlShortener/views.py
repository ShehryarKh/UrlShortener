from django.shortcuts import render, redirect
#url.models
from .models import Url
from django.views.generic import View

from .forms import UrlForm

# Create your views here.


class UrlView(View):
	template = "index.html"
	form = UrlForm

	def get(self,request,shortened=''):
		print("in get")

		context={
			"shortened":shortened,

			"url_form":UrlForm
		}
		return render(request,self.template,context)


	def post(self,request):
		print("in post")

		form = UrlForm(request.POST)

		if form.is_valid():
			test= form.save()


			return redirect("blog:index",shortened=test.short)


class ShortUrl(View):
	def get(self, request,short):
		url = Url.objects.get(short=short)
		if url is None:
			redirect('index')
		else:

			return redirect(url.actual)






