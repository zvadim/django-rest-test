from django.contrib.gis.geos import Point
from django.test import TestCase
from cities.models import PostalCode, Country


class TestAppTest(TestCase):

    def setUp(self):
        c = Country.objects.create(code='US', code3='USA', population=10000)
        PostalCode.objects.create(country=c, code=99553, region_name='Alaska', location=Point(1, 1))

    def test_postcode(self):
        self.assertEqual(PostalCode.objects.filter(country__code='US', code=99553)[0].region_name, 'Alaska')
