"""Tests for Marvel Cinematic Universe app."""

import unittest
from server import app



#test functions that render a template.

def test_homepage(self):
    """Tests to see if homepage renders."""

    result = self.client.get('/')

    self.assertEqual(result.status_code, 200)
    self.assertIn('text/html', result.headers['Content-Type'])
    self.assertIn('<a href="/movie_list" class="btn btn-lg btn-primary">ENTER</a>', result.data)

def test_movie_list(self):
    """Tests to see if movie_list page renders."""

    result = self.client.get('/movie_list')

    self.assertEqual(result.status_code, 200)
    self.assertIn('text/html'), result.headers['Content-Type'])
    self.assertIn('MOVIES',result.data)

def test_characters(self):
    """Test to see if the characters_list page renders."""

    result = self.client.get('/characters')

    self.assertEqual(results.status_code, 200)
    self.assertIn('text/html'), result.headers['Content-Type'])
    self.assertEqual('CHARACTERS', result.data)