from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.activity = Activity.objects.create(user=self.user, activity_type='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_activity_str(self):
        self.assertEqual(str(self.activity), 'testuser - Running')

    def test_leaderboard_str(self):
        self.assertEqual(str(self.leaderboard), 'testuser - 100')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
