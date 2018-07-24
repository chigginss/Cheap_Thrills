

class IntegrationTests(unittest.TestCase):
    """Examples of integration tests: testing Flask server."""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<title>Cheap Thrills!</title>', result.data)