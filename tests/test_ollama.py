import unittest
from unittest.mock import patch
from app.ollama_client import get_ollama_response

class TestOllamaClient(unittest.TestCase):
    @patch('requests.post')
    def test_get_response(self, mock_post):
        mock_post.return_value.json.return_value = {"response": "Test response"}
        result = get_ollama_response("test")
        self.assertEqual(result, "Test response")