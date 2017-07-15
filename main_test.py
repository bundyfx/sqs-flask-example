# -*- coding: utf-8 -*-
import pytest

import main

@pytest.fixture
def client():
    return main.app.test_client()

def test_urls(client):
    r = client.get('/')
    assert r.status_code == 200
