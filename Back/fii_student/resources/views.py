from .models import Resources
from django.shortcuts import render
from django.urls import reverse
from pprint import pprint

def show_resources(request):
    post_url = reverse('resources_show')
    generic_objects = Resources.objects.all()
    # filtered_objects = generic_objects
    # filtered = table = None
    #
    # filtered = NewsFilter(request.GET, queryset=generic_objects)
    # filtered_objects = filtered.qs
    #
    # table = NewsTable(filtered_objects)
    # RequestConfig(request, paginate={"per_page": 25}).configure(table)
    #
    # tdelta = sum((float(i['time']) for i in connection.queries))
    # setattr(table, 'tdelta', tdelta)
    return render(request, 'show_resources.html',
                  {'title': 'Resources',
                   'post_url_name': 'resources_show',
                   'post_url': post_url,
                   'objects': generic_objects,
                   # 'filter': filtered,
                   })
