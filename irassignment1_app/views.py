import pysolr
from django.shortcuts import render

def search_form(request):
    return render(request, 'search_form.html')

def search_results(request):
    query = request.GET.get('q', '')
    solr = pysolr.Solr('http://localhost:8983/solr/mycore')
    results = solr.search(query,df = "title")
    return render(request, 'search_results.html', {'results': results})
