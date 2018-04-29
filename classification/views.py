from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse

class HomeView(TemplateView):
    template_name = 'webservice.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

home = HomeView.as_view()

class ClassificationView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

    def post(request, self, *argv, **kwargs):
        return JsonResponse({'status': 'ok'})

classification = ClassificationView.as_view()
