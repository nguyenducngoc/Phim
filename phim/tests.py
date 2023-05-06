from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class LoginTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='ngocnd',
            email='123@dmail.com',
            password='ngocbityto'
        )
        
    def test_login_success(self):
        user = authenticate(username='testuser', password='testpass')
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)
        
    def test_login_failure(self):
        user = authenticate(username='testuser', password='wrongpass')
        self.assertIsNone(user)
