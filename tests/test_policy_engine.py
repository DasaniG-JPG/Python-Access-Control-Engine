import unittest

from policy_engine import evaluate_access


class TestAccessPolicy(unittest.TestCase):
    def test_admin_with_mfa_is_allowed_on_approved_port(self):
        allowed, _ = evaluate_access("alice", "admin", True, 22)
        self.assertTrue(allowed)

    def test_admin_without_mfa_is_denied(self):
        allowed, _ = evaluate_access("alice", "admin", False, 22)
        self.assertFalse(allowed)

    def test_support_with_mfa_can_use_https(self):
        allowed, _ = evaluate_access("sam", "support", True, 443)
        self.assertTrue(allowed)

    def test_support_without_mfa_is_denied(self):
        allowed, _ = evaluate_access("sam", "support", False, 443)
        self.assertFalse(allowed)

    def test_support_cannot_use_ssh(self):
        allowed, _ = evaluate_access("sam", "support", True, 22)
        self.assertFalse(allowed)

    def test_user_can_use_http(self):
        allowed, _ = evaluate_access("jordan", "user", False, 80)
        self.assertTrue(allowed)

    def test_user_cannot_use_rdp(self):
        allowed, _ = evaluate_access("jordan", "user", False, 3389)
        self.assertFalse(allowed)

    def test_blank_username_is_denied(self):
        allowed, reason = evaluate_access("", "user", False, 80)
        self.assertFalse(allowed)
        self.assertIn("blank", reason.lower())

    def test_invalid_role_is_denied(self):
        allowed, reason = evaluate_access("casey", "root", True, 443)
        self.assertFalse(allowed)
        self.assertIn("invalid role", reason.lower())

    def test_unapproved_port_is_denied(self):
        allowed, reason = evaluate_access("casey", "admin", True, 8080)
        self.assertFalse(allowed)
        self.assertIn("not approved", reason.lower())


if __name__ == "__main__":
    unittest.main()
