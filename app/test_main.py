import unittest

from main import create_event


class TestCreateEvent(unittest.TestCase):

    def test_event_has_required_fields(self):
        event = create_event("login", "info")

        self.assertIn("timestamp", event)
        self.assertEqual(event["event_type"], "login")
        self.assertEqual(event["severity"], "info")


if __name__ == "__main__":
    unittest.main()
