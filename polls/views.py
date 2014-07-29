from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Poll, Choice

# Create your views here.

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_poll_list'

  def get_queryset(self):
    """ return the last five published polls """
    return Poll.objects.order_by('-pub_date')[:5]

def index(request):
  latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
  context = { "latest_poll_list": latest_poll_list}
  return render(request, 'polls/index.html', context)
  
def detail(request, poll_id):
  poll = get_object_or_404(Poll, pk=poll_id)
  return render(request, 'polls/detail.html', {'poll': poll})
    
def results(request, poll_id):
  poll = get_object_or_404(Poll, pk=poll_id)
  return render(request, 'polls/results.html', {'poll': poll})
    
def vote(request, poll_id):
  poll = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = poll.choice_set.get(pk=request.POST['choice'])
  except KeyError, Choice.DoesNotExist:
    return render(request, 'polls/detail.html', 
      {
      'poll': poll, 
      'error_message': 'You did not select a choice'
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))