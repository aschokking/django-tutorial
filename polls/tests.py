import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Poll

def create_poll(question, days):
    return Poll.objects.create(question=question, 
                               pub_date=timezone.now() + datetime.timedelta(days=days))

class PollViewTests(TestCase):
    def test_index_view_with_no_polls(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available right now.")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_a_past_poll(self):
        create_poll(question="past", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: past>'])
            
    def test_index_view_with_a_future_poll(self):
        create_poll(question="future", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls available right now.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

class PollIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_poll(self):
        future_poll = create_poll(question="future", days=30)
        response = self.client.get(reverse('polls:detail', args=(future_poll.id,)))        
        self.assertEquals(response.status_code, 404)
        
    def test_detail_view_with_a_past_poll(self):
        future_poll = create_poll(question="past", days=-30)
        response = self.client.get(reverse('polls:detail', args=(future_poll.id,)))        
        self.assertEquals(response.status_code, 200)
        
class PollMethodTests(TestCase):
	def test_was_published_recently_with_future_poll(self):
		"""
		was_published_recently should return false for polls with future
		published dates
		"""
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)

	def test_was_published_recently_with_old_poll(self):
		"""
		was_published_recently should return False for polls with pub_dates older than 1 day
		"""
		old_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=-2))
		self.assertEqual(old_poll.was_published_recently(), False)