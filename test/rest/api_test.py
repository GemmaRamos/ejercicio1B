import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "15", "ERROR ADD"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "1.5", "ERROR ADD"
        )

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/5/0"  # Intentando dividir por 0
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.assertNotEqual(
                response.status, http.client.OK, f"Se esperaba un error en {url}"
            )
            self.assertEqual(
                response.status, 406, f"Se esperaba un error HTTP 406 en {url}"
            )
        except HTTPError as e:
            self.assertEqual(
                e.code, 406, f"Se esperaba un error HTTP 406 en {url}"
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
