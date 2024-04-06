from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

class CreateNoteTemplateTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_note_form(self):
        response = self.client.get(reverse('create_note'))  # replace 'create_note' with the actual name of your view

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the form is in the response
        self.assertContains(response, '<form method="post" action="">')

        # Check that the CSRF token is in the response
        self.assertContains(response, '{% csrf_token %}')

        # Check that the form fields are in the response
        self.assertContains(response, '<textarea id="')
        self.assertContains(response, '<input class="form-input')

        # Check that the submit button is in the response
        self.assertContains(response, '<button type="submit"')