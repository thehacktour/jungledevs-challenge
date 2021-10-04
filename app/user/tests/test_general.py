from django.test import TestCase
from django.urls import reverse

class AuthorListViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/oficial/user/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_list.html')
