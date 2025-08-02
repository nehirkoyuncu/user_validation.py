# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains # type: ignore

print("validate_name\n")
print(validate_name.__doc__)
print("--------------------\n")

print("validate_email\n")
print(validate_email.__doc__) 
print("--------------------\n")

print("validate_password\n")
print(validate_password.__doc__)

# The top level domains variable is used in validate_email to approve only certain email domains
print(top_level_domains)
def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("Please enter your name correctly!")
    if not validate_email(email):
        raise ValueError("Please enter your e-mail correctly!")
    if not validate_password(password):
        raise ValueError("Please enter your password correctly!")
    return True

def register_user(name, email, password):
    try:
        if validate_user(name, email, password):
            return {'Name': name, 'Email': email, 'Password': password}
    except ValueError:
        return False