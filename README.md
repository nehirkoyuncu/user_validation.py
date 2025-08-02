# User Registration and Validation System 

This project provides a simple yet effective user registration system with input validation in Python. It ensures user input for **name**, **email**, and **password** is properly validated before creating a user account.

---

##  Features

- `validate_user(name, email, password)`: Validates user input by calling helper functions.
- `register_user(name, email, password)`: Handles user registration using `validate_user`.
- Modular validation functions for name, email, and password.

---

##  Validation Rules

- `validate_name(name)`
  - Must be a non-empty string.
  - Should not contain only whitespace.
  
- `validate_email(email)`
  - Must contain `"@"` and `"."` characters.
  - Should be at least 5 characters long.

- `validate_password(password)`
  - Must be at least 8 characters long.
  - Should contain at least one number and one uppercase letter.

---

##  Function Descriptions

### `validate_user(name, email, password)`

Validates user input using helper functions.  
- Returns `True` if all validations pass.
- Raises `ValueError` with a descriptive message if any check fails.

### `register_user(name, email, password)`

Registers a new user.
- Calls `validate_user()` first.
- If validation fails, returns `False`.
- If successful, returns a `dict` with the keys: `name`, `email`, and `password`.

---


