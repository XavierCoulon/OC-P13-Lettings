from pytest_django.asserts import assertContains, assertTemplateUsed

from django.test import Client
from django.urls import reverse


def test_index():
    client = Client()
    response = client.get(reverse("index"))

    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")
    assertContains(response, "<title>Holiday Homes</title>")
