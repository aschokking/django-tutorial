import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

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