from django.shortcuts import render,redirect


# 어떤 기능을 만들어 주는 곳
# urls.py 내가 views.py 만든 기능이 어떤 url로 접속했을 때 동작하게 할 것이냐?
# Create your views here.

from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

from django.views.generic.list import ListView
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

from django.views.generic.edit import CreateView,UpdateView,DeleteView

class BookmarkCreateView(CreateView):
    model = Bookmark
    template_name_suffix = '_create'
    fields = ['site_name',"url"]

    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark')
        else:
            return self.render_to_response({'form':form})

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'


from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    from django.urls import reverse_lazy
    model = Bookmark
    success_url = reverse_lazy("bookmark:index")

