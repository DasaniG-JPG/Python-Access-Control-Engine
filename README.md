x Python Access Control Engine

A small Python cybersecurity project that demonstrates role-based access control (RBAC), multi-factor authentication checks, service-port restrictions, and input validation.

This project began as a cybersecurity lab exercise and was expanded into a cleaner, testable policy engine suitable for demonstrating secure-programming fundamentals.

x What It Does

The program evaluates four pieces of information:

- Username
- User role (`admin`, `support`, or `user`)
- MFA status
- Requested service port

It then returns either `ALLOW` or `DENY` with an explanation.

x Access Policy

| Role | MFA Required? | Allowed Ports |
|---|---|---|
| Admin | Yes | 22, 80, 443, 3389 |
| Support | Yes | 443, 3389 |
| User | No | 80, 443 |

Any request using an unapproved port is denied.

x Security Concepts Demonstrated

- Role-Based Access Control (RBAC)
- Least privilege
- Multi-factor authentication enforcement
- Allowlisting
- Input validation
- Explicit deny behavior
- Separation of policy logic from user input
- Automated unit testing

x Project Structure

```text
python-access-control-engine/
├── policy_engine.py
├── tests/
│   └── test_policy_engine.py
├── README.md
├── .gitignore
└── LICENSE
```

x Run the Program

```bash
python policy_engine.py
```

Example:

```text
=== Access Policy Engine ===
Enter username: jordan
Enter role (admin/support/user): user
Is MFA enabled? (yes/no): no
Enter requested service port: 443
ALLOW: User may access approved web services.
```

x Run the Tests

From the project directory:

```bash
python -m unittest discover -s tests -v
```

x Why I Built This

I created this project while learning how authentication, authorization, and least-privilege policies can be represented in code. I later refactored the original lab into reusable functions and added automated tests so the policy logic could be verified independently from user input.

x Possible Future Improvements

- Load policy rules from a JSON or YAML configuration file
- Add audit logging
- Add timestamps and request IDs
- Support additional roles and services
- Build a simple GUI or web interface
- Export access decisions for security monitoring

x Disclaimer

This project is intended for educational use. It is not a replacement for a production identity and access management system.
