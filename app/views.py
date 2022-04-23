from .tasks import tiny_url
from django.urls import reverse_lazy
from .forms import UrlForm
from django.views.generic import CreateView, ListView
from .models import Url

class UrlCreate(CreateView):
    form_class = UrlForm
    template_name = 'app/base.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_list'] = Url.objects.all()[::-1]
        return context

    def form_valid(self, form):
        x = form.save()
        tiny_url.delay(x.url, x.pk)
        return super().form_valid(form)