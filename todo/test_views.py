from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from .models import Item
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'todo_list.html')

    def test_get_add_item_page(self):
        page = self.client.get('/add', follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')

    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()

        page = self.client.get("/edit/{0}".format(item.id), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/99", follow=True)
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        response = self.client.post("/add/", {"name": "Create a Test"}, follow=True)
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertEqual(item.done, False)
        id = item.id
        data = {
            "name": 'Create a test!',
            "done": True,
        }
        response = self.client.post("/edit/{0}/".format(id), data, follow=True)
        self.assertEqual(response.status_code, 200)

        item = get_object_or_404(Item, pk=1)
        # response = self.client.post("/edit/{0}".format(id), {"name": "Create a Test!", "done": True})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, True)
        self.assertEqual(item.name, "Create a test!")

    def test_toggle_status(self):
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertEqual(item.done, False)
        id = item.id
        response = self.client.post("/toggle/{0}/".format(id))
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, True)
        self.assertEqual(item.name, "Create a Test")
