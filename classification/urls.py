from django.conf.urls import url
from classification import views as classification

urlpatterns = [
    url(r'^$', classification.home, name='home'),
    url(r'^classification/$', classification.classification, name='classification'),
]
