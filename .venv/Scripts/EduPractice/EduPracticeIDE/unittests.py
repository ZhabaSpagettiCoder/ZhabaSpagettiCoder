from django.test import TestCase, Client
from django.urls import reverse
from .models import Inputdatauser, Typesofusers, Inputdatarequests, Techt
import json

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_type = Typesofusers.objects.create(id=0)  # Создаем тип пользователя
        self.user = Inputdatauser.objects.create(
            fio='Test User',
            phone='1234567890',
            login='testuser@example.com',
            password='password123',
            type=self.user_type,
            ID='ABC'
        )

    def test_start_page(self):
        response = self.client.get(reverse('StartPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Auth.html')

    def test_registration_page(self):
        response = self.client.get(reverse('Registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reg.html')

    def test_db_reg_response(self):
        response = self.client.post(reverse('DBRegResponse'), {
            'FullName': 'New User',
            'Email': 'newuser@example.com',
            'PhoneNumber': '0987654321',
            'Password1': 'newpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registration end successfull")
        self.assertTrue(Inputdatauser.objects.filter(login='newuser@example.com').exists())

    def test_menu_user(self):
        # Устанавливаем cookie
        self.client.cookies['Data'] = json.dumps(['Test User', '1234567890', 'testuser@example.com', 'password123', 'hash_value', 'client_id'])
        response = self.client.get(reverse('Menu'), {'hash': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'PanelView.html')

    def test_menu_admin(self):
        # Устанавливаем cookie
        self.client.cookies['Data'] = json.dumps(['Test User', '1234567890', 'testuser@example.com', 'password123', 'hash_value', 'client_id'])
        response = self.client.get(reverse('Menu'), {'hash': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'AdminPanel.html')

    def test_auth_try_success(self):
        response = self.client.post(reverse('AuthTry'), {
            'login': 'testuser@example.com',
            'pass': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Проверка редиректа
        self.assertTrue('Data' in response.cookies)

    def test_auth_try_failure(self):
        response = self.client.post(reverse('AuthTry'), {
            'login': 'testuser@example.com',
            'pass': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Password is incorrect!")

    def test_add_page(self):
        response = self.client.get(reverse('Add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RequestUser.html')

    def test_add_super_page(self):
        response = self.client.get(reverse('AddSuper'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RequestAdmin.html')