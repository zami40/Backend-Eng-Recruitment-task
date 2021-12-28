from django.db import models
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse


from mobiles.models import Mobile

# Create your views here.
class MobileList(ListView):
    model = Mobile
    context_object_name = 'mobiles'

class MobileDetail(DetailView):
    model = Mobile
    context_object_name = 'mobile'
    template_name = 'mobiles/mobile.html'

class MobileCreate(CreateView):
    model = Mobile
    fields = '__all__'
    success_url = reverse_lazy('mobiles')

class MobileUpdate(UpdateView):
    model = Mobile
    fields = '__all__'
    success_url = reverse_lazy('mobiles')  


class MobileDelete(DeleteView):
    model = Mobile
    context_object_name = 'mobile'
    success_url = reverse_lazy('mobiles')


class MobileSearch(View):
    def get(self, request, *args, **kwargs):
        search_input = request.GET.get('search')
        if search_input:
            mobiles = Mobile.objects.filter(model_name__icontains=search_input)
            if mobiles:
                table = '<tr><th>Mobile Name</th><th></th></tr>'
                for mobile in mobiles:
                    table += '<tr><td>' + mobile.model_name + '</td><td><a href="' + reverse('mobile', kwargs={'pk':mobile.id}) + '">View</a></td>'
                    table += '<td><a href="' + reverse('mobile-update', kwargs={'pk':mobile.id}) + '">Update</a></td>'
                    table += '<td><a href="'+ reverse('mobile-delete', kwargs={'pk':mobile.id}) + '">Delete</a></td></tr>'
                return HttpResponse(table)
            else:
                no_data = '<h3>No Mobiles in the list</h3>'
                return HttpResponse(no_data)