from django.views.generic import TemplateView
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from django.contrib import messages
from django.urls import reverse
import json

class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

home = HomeView.as_view()

class ClassificationView(TemplateView):
    template_name = 'classification.html'
    accuracy_score = 0
    results = []

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        context = super(ClassificationView, self).get_context_data(**kwargs)
        context['accuracy_score'] = self.accuracy_score
        context['results'] = self.results
        return context

    def post(self, request, *arg, **kwargs):
        csvfile = request.FILES['csvfile']
        if not csvfile.name.endswith('.csv'):
            messages.error(request, 'Please import a CSV file')
            return HttpResponseRedirect(reverse("classification"))

        df = pd.read_csv(csvfile, header=None, names=['label', 'words'])
        vectorizer = joblib.load('train/vectorizer-aws.pkl')
        X = vectorizer.transform(df.words.values.astype('U'))
        y = df.label
        clf = joblib.load('train/model-aws.pkl')
        y_pred = clf.predict(X)
        y_pred_prob = clf.predict_proba(X)

        self.results = []
        for i in range(len(y)):
            self.results.append({'true': y[i], 'pred': y_pred[i], 'confidence': max(y_pred_prob[i])})

        self.accuracy_score = accuracy_score(y, y_pred)

        return self.render_to_response(self.get_context_data(**kwargs))

classification = ClassificationView.as_view()
