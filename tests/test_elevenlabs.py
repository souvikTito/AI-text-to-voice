import unittest
from unittest.mock import patch
from app.elevenlabs_client import clean_markdown

class TestElevenLabsClient(unittest.TestCase):
    def test_clean_markdown(self):
        self.assertEqual(clean_markdown("**bold**"), "bold")
        self.assertEqual(clean_markdown("`code`"), "code")