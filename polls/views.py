from django.shortcuts import render
from django.http import HttpResponse, Http404

from polls.models import Poll

# Create your views here.

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
    
def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})
    
def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)
    
def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)