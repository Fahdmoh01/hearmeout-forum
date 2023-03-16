from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
            context_dict={}
            context_dict['boldmessage']='We out here fighting for our lives!'
            return render(request, 'forum/index.html/', context= context_dict)