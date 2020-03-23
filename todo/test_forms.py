from django.test import TestCase
from.forms import ItemForm


# Create your tests here.
class TestToDoItemForm(TestCase):

    # verify you can create an item by just passing in a name
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid())

    # verify that you must have something in the name to create an item
    def test_correct_message_for_missing_name(self):
        form=ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])



