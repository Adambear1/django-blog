from django import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from blogging.models import Post


class ListView():
    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower
        context = {model_list_name: Post.objects.all()}
        return render(request, self.template_name, context)


class DetailView():
    def as_view(self):
        return self.get

    def get(self, request, *args, **kwargs):
        if "pk" in args:
            model_list_name = self.model.__name__.lower
            context = {model_list_name: Post.objects.get(pk=args["pk"])}
            return render(request, self.template_name, context)
        model_list_name = self.model.__name__.lower
        context = {model_list_name: Post.objects.all().order_by(
            "-created_date").filter("published_date" != None)}
        return render(request, self.template_name, context)


class BloggingListView(ListView):
    model = Post
    template_name = "blogging/list.html"


class BlogginDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
