"""Simple role-based access control policy engine.

Evaluates a username, role, MFA status, and requested service port
to determine whether access should be allowed or denied.
"""

VALID_ROLES = {"admin", "support", "user"}
VALID_PORTS = {22, 80, 443, 3389}
SUPPORT_PORTS = {443, 3389}
USER_PORTS = {80, 443}


def evaluate_access(username: str, role: str, mfa_enabled: bool, port: int) -> tuple[bool, str]:
    """Evaluate a request against the access policy.

    Returns:
        tuple[bool, str]: (allowed, reason)
    """
    username = username.strip()
    role = role.strip().lower()

    if not username:
        return False, "Username cannot be blank."

    if role not in VALID_ROLES:
        return False, "Invalid role."

    if not 1 <= port <= 65535:
        return False, "Port must be between 1 and 65535."

    if port not in VALID_PORTS:
        return False, "Requested service port is not approved."

    if role == "admin" and mfa_enabled:
        return True, "Authenticated admin may access this approved service."

    if role == "support" and mfa_enabled and port in SUPPORT_PORTS:
        return True, "Support role may access this approved service with MFA."

    if role == "user" and port in USER_PORTS:
        return True, "User may access approved web services."

    return False, "Request does not meet the access policy."


def get_port() -> int | None:
    """Read and validate a port number from user input."""
    port_input = input("Enter requested service port: ").strip()

    if not port_input.isdigit():
        print("DENY: Port must be a number.")
        return None

    return int(port_input)


def get_mfa_status() -> bool | None:
    """Read MFA status from user input."""
    mfa_input = input("Is MFA enabled? (yes/no): ").strip().lower()

    if mfa_input not in {"yes", "no"}:
        print("DENY: MFA status must be yes or no.")
        return None

    return mfa_input == "yes"


def main() -> None:
    """Run the interactive access-control checker."""
    print("=== Access Policy Engine ===")

    username = input("Enter username: ").strip()
    role = input("Enter role (admin/support/user): ").strip().lower()

    mfa_enabled = get_mfa_status()
    if mfa_enabled is None:
        return

    port = get_port()
    if port is None:
        return

    allowed, reason = evaluate_access(username, role, mfa_enabled, port)
    decision = "ALLOW" if allowed else "DENY"
    print(f"{decision}: {reason}")


if __name__ == "__main__":
    main()
