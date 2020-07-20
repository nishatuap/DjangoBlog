from django.contrib.auth import get_user_model  #allows you to create  virtual user
from django.test import SimpleTestCase, TestCase #Testcase invloves database / SimpleTestcase doesnt
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self): #ychouf url existe wala lé
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email) #Created a user
        self.assertEqual(get_user_model().objects.all().count(), 1)#Testing if one user got created
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)  #Checking if the username created equals the same username declared
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)