<<<<<<< HEAD
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
    
=======
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

class DetailView(generic.DetailView):
  model = Poll
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Poll
  template_name = 'polls/results.html'
  
>>>>>>> 608791288c376b1b228d38d626f2f2f41c514e40
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
