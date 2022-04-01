from django.test import TestCase
from .models import *
from datetime import datetime
from pprint import pprint as pp
from django.urls import reverse
class TestUser(TestCase):

  def setUp(self) -> None:
    self.user = User.objects.create_user(username="test", password="121212")  

  def test_can_user(self):    
    self.assertIsInstance(self.user, User)

  def test_user_has_profile(self):
    self.assertIsInstance(self.user.profile, Profile)




class TestProfile(TestCase):
  def setUp(self) -> None:
      self.user = User.objects.create_user(username="test", password="121212")  

  def test_profile_exists(self):
    self.assertIsInstance(self.user.profile, Profile)

  def test_profile_links_to_user(self):
    self.assertTrue(self.user == self.user.profile.user)

  def test_profile_has_weights(self):
    count_of_records = self.user.profile.weights.count()
    self.assertTrue(count_of_records == 0)



class TestWeight(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(username="test", password="121212")

  def test_can_add_weight(self):
    entry_date = datetime.now()     
    self.user.profile.weights.create(lbs=120, entry_date=entry_date)
    self.assertTrue(self.user.profile.weights.count() == 1)


class TestLoginView(TestCase):

  def test_can_render_view(self):
    response = self.client.get(reverse('login'))
    print(response)
    self.assertTemplateUsed(response, 'registration/login.html')
    