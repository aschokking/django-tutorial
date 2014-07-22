from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You're at the poll index, welcome")
    
def detail(request, poll_id):
    return HttpResponse("Detail for poll %s" % poll_id)
    
def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)
    
def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)