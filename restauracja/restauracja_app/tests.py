from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from django import urls
from . import views
from rest_framework import status
from .models import Kategorie
from django.utils.http import urlencode
from django.contrib.auth.models import User
# Create your tests here.

class KategorieTests(APITestCase):

    def post_kategorie(self, id, name, client):
        url = reverse(views.RestauracjaKategorieList.view_name)
        data = {'Kategorie_id': id,'Nazwa': name}
        response = client.post(url, data, format='json')
        return response

    def test_post_get_kategorie(self):
        User.objects.create_superuser('admin', 'bla.wp.pl', 'ab1234567')
        client = APITestCase()
        client.login(username='admin', password='ab1234567')
        new_kategoria = 'Napoje'
        response = self.post_kategorie(99, new_kategoria, client)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kategorie.objects.count() == 1
        assert Kategorie.objects.get().Nazwa == new_kategoria

    def test_unique_id_kategorie(self):
        new_id = '1'
        new_kategoria = 'Napoje'
        response1 = self.post_kategorie(new_id, new_kategoria)
        assert response1.status_code == status.HTTP_201_CREATED
        response2 = self.post_kategorie(new_id, new_kategoria)
        assert  response2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_nazwa_kategorie(self):
        new_kategoria1 = 'Napoje'
        new_kategoria2 = 'Soki'
        self.post_kategorie(10, new_kategoria1)
        self.post_kategorie(11, new_kategoria2)
        filter_by_name = {'Nazwa': new_kategoria1}
        url = '{0}?{1}'.format(reverse(views.RestauracjaKategorieList.view_name), urlencode(filter_by_name))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['Nazwa'] == new_kategoria1

    def test_update_kategorie(self):
        new_kategoria = 'Napoje'
        new_id = '15'
        response = self.post_kategorie(new_id, new_kategoria)
        url = urls.reverse(views.RestauracjaKategorieDetail.view_name, None, {response.data['Kategorie_id']})
        updated_Nazwa = 'Soki'
        data = {'Nazwa': updated_Nazwa}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['Nazwa'] == updated_Nazwa



