from rest_framework import status
from rest_framework.test import APITestCase

class VisitedDomainsTests(APITestCase):

    def test_get_visited_domains(self):

        url = 'http://127.0.0.1:8000/api/v1/visited_domains?from=1&to=1980599411'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_visited_domains_without_params(self):

        url = 'http://127.0.0.1:8000/api/v1/visited_domains'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_visited_domains_params_not_int(self):

        url = 'http://127.0.0.1:8000/api/v1/visited_domains?from=test1&to=1980599411'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class VisitedLinksTests(APITestCase):

    def test_post_visited_links(self):

        url = 'http://127.0.0.1:8000/api/v1/visited_links'
        USER_DATA = {
            "links": [
                "https://ya.ru",
                "https://ya.ru?q=123",
                "funbox.ru",
                "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
            ]
        }
        response = self.client.post(url, USER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_visited_links_invalid_json(self):

        url = 'http://127.0.0.1:8000/api/v1/visited_links'
        USER_DATA = {
            "urls": [
                "https://ya.ru",
                "https://ya.ru?q=123",
                "funbox.ru",
                "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
            ]
        }
        response = self.client.post(url, USER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)