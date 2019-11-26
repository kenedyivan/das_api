from django.test import TestCase
from django.test import Client

# Create your tests here.
from api.models import District, SubCounty


class DistrictsTestCase(TestCase):
    def setUp(self):
        self.district_name_1 = 'Tongo'
        self.district_name_2 = 'Katakwi'
        District.objects.create(name=self.district_name_1)
        District.objects.create(name=self.district_name_2)

    def test_can_create_districts(self):
        tongo = District.objects.get(name=self.district_name_1)
        katakwi = District.objects.get(name=self.district_name_2)
        self.assertEqual(tongo.name, self.district_name_1)
        self.assertEqual(katakwi.name, self.district_name_2)

    def test_can_edit_district(self):
        self.edit_district_1_name = 'Makila'
        tongo = District.objects.get(name=self.district_name_1)
        tongo.name = self.edit_district_1_name
        tongo.save()
        self.assertEqual(tongo.name, self.edit_district_1_name)

    def test_can_delete_district(self):
        katakwi = District.objects.get(name=self.district_name_2)
        katakwi.delete()
        self.assertEqual(District.objects.count(), 1)

    def test_can_list_districts(self):
        client = Client()
        response = client.get('/api/v1/districts')
        self.assertEqual(response.status_code, 200)


class SubCountiesTestCase(TestCase):
    def setUp(self):
        self.district_name = 'Mukula'
        self.sub_county_name_1 = 'Mujuni'
        self.sub_county_name_2 = 'Muloki'
        district = District.objects.create(name=self.district_name)
        self.district_id = district.id
        sub1 = SubCounty(id=None, name=self.sub_county_name_1, district=district)
        sub1.save()
        sub2 = SubCounty(id=None, name=self.sub_county_name_2, district=district)
        sub2.save()

    def test_can_create_sub_county(self):
        sub = SubCounty.objects.get(name=self.sub_county_name_1)
        self.assertEqual(sub.name, self.sub_county_name_1)

    def test_can_list_all_sub_counties(self):
        client = Client()
        response = client.get('/api/v1/sub-counties')
        self.assertEqual(response.status_code, 200)

    def test_can_list_sub_counties_for_a_district_with_id(self):
        client = Client()
        response = client.get('/api/v1/districts/' + str(self.district_id) + '/sub-counties')
        self.assertEqual(response.status_code, 200)

    def test_can_edit_sub_county(self):
        self.edit_sub_county_name = 'Moro'
        mujuni = SubCounty.objects.get(name=self.sub_county_name_1)
        mujuni.name = self.edit_sub_county_name
        mujuni.save()
        self.assertEqual(mujuni.name, self.edit_sub_county_name)

    def test_can_delete_sub_county(self):
        muloki = SubCounty.objects.get(name=self.sub_county_name_2)
        muloki.delete()
        self.assertEqual(District.objects.count(), 1)
