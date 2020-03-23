from django.test import TestCase
from .models import Item


class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertEqual(item.done, False)

    def test_done_set_to_False(self):
        item = Item(name='Create a Test',done=True)
        item.save()
        self.assertEqual(item.name, 'Create a Test')
        self.assertEqual(item.done, True)

    def test_item_as_string(self):
        item = Item(name='Create a Test')
        item.save()
        self.assertEqual(str(item), 'Create a Test')