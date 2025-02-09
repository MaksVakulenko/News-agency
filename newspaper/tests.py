from django.test import TestCase, Client
from django.urls import reverse
from .models import Newspaper, Topic, Redactor


class NewspaperCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.redactor = Redactor.objects.create_user(
            username="testuser", password="testpass123", years_of_experience=5
        )
        self.topics = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(
            title="Test News", content="Test Content"
        )
        self.newspaper.topics.add(self.topics)
        self.newspaper.publishers.add(self.redactor)
        self.client.login(username="testuser", password="testpass123")

    def test_create_newspaper(self):
        response = self.client.post(
            reverse("newspaper:newspaper-create"),
            {
                "title": "New News",
                "content": "New Content",
                "topics": [self.topics.id],
                "publishers": [self.redactor.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Newspaper.objects.filter(title="New News").exists())

    def test_create_newspaper_invalid_data(self):
        response = self.client.post(
            reverse("newspaper:newspaper-create"),
            {"title": "", "content": "", "topics": [], "publishers": []},
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.errors["title"])

    def test_read_newspaper(self):
        response = self.client.get(
            reverse("newspaper:newspaper-detail", args=[self.newspaper.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["newspaper"], self.newspaper)

    def test_update_newspaper(self):
        response = self.client.post(
            reverse("newspaper:newspaper-update", args=[self.newspaper.pk]),
            {
                "title": "Updated News",
                "content": "Updated Content",
                "topics": [self.topics.id],
                "publishers": [self.redactor.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.newspaper.refresh_from_db()
        self.assertEqual(self.newspaper.title, "Updated News")

    def test_delete_newspaper(self):
        response = self.client.post(
            reverse("newspaper:newspaper-delete", args=[self.newspaper.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Newspaper.objects.filter(pk=self.newspaper.pk).exists()
        )


class TopicCRUDTests(TestCase):
    def setUp(self):
        self.topics = Topic.objects.create(name="Test Topic")

    def test_crud_operations(self):
        new_topic = Topic.objects.create(name="New Topic")
        self.assertTrue(Topic.objects.filter(name="New Topic").exists())

        topic = Topic.objects.get(name="Test Topic")
        self.assertEqual(topic.name, "Test Topic")

        topic.name = "Updated Topic"
        topic.save()
        self.assertEqual(Topic.objects.get(pk=topic.pk).name, "Updated Topic")

        topic.delete()
        self.assertFalse(Topic.objects.filter(pk=topic.pk).exists())


class RedactorCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = Redactor.objects.create_superuser(
            username="admin", password="admin123", years_of_experience=5
        )
        self.client.login(username="admin", password="admin123")

        self.test_redactor = Redactor.objects.create(
            username="testredactor",
            first_name="Test",
            last_name="Redactor",
            email="test@example.com",
            years_of_experience=3,
        )

    def test_create_redactor(self):
        response = self.client.post(
            reverse("newspaper:redactor-create"),
            {
                "username": "newredactor",
                "password1": "testpass123",
                "password2": "testpass123",
                "first_name": "New",
                "last_name": "Redactor",
                "email": "new@example.com",
                "years_of_experience": 2,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Redactor.objects.filter(username="newredactor").exists()
        )

    def test_create_redactor_invalid_data(self):
        response = self.client.post(
            reverse("newspaper:redactor-create"),
            {
                "username": "",
                "password1": "",
                "password2": "",
                "years_of_experience": "",
            },
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertTrue(form.errors["username"])

    def test_read_redactor(self):
        response = self.client.get(
            reverse("newspaper:redactor-detail", args=[self.test_redactor.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["redactor"], self.test_redactor)

    def test_update_redactor(self):
        response = self.client.post(
            reverse("newspaper:redactor-update", args=[self.test_redactor.pk]),
            {
                "username": "testredactor",
                "first_name": "Updated",
                "last_name": "Name",
                "email": "updated@example.com",
                "years_of_experience": 4,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.test_redactor.refresh_from_db()
        self.assertEqual(self.test_redactor.first_name, "Updated")
        self.assertEqual(self.test_redactor.years_of_experience, 4)

    def test_delete_redactor(self):
        response = self.client.post(
            reverse("newspaper:redactor-delete", args=[self.test_redactor.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Redactor.objects.filter(pk=self.test_redactor.pk).exists()
        )


class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.redactor = Redactor.objects.create_user(
            username="testuser", password="testpass123", years_of_experience=5
        )
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")

    def test_user_login(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.url.startswith(reverse("newspaper:newspaper-list"))
        )

        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)

    def test_user_logout(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("login")))

        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)
