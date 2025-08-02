# List of allowed top-level domains for email validation
top_level_domains = ['com', 'org', 'net', 'edu', 'gov']

def validate_name(name):
    """
    Validates the user's name.
    Requirements:
    - Must be between 2 and 50 characters long
    - Can only contain letters and spaces
    - Must start with a capital letter
    
    Args:
        name (str): The name to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(name, str):
        return False
    if len(name) < 2 or len(name) > 50:
        return False
    if not name.replace(' ', '').isalpha():
        return False
    if not name[0].isupper():
        return False
    return True

def validate_email(email):
    """
    Validates the user's email address.
    Requirements:
    - Must contain exactly one @ symbol
    - Domain must have a valid top-level domain
    - Local part (before @) must be at least 1 character
    - Domain part (after @) must be at least 3 characters
    
    Args:
        email (str): The email to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    if not local_part or len(local_part) < 1:
        return False
    
    if '.' not in domain_part:
        return False
    
    domain_parts = domain_part.split('.')
    if len(domain_parts) < 2:
        return False
    
    tld = domain_parts[-1].lower()
    if tld not in top_level_domains:
        return False
    
    return True

def validate_password(password):
    """
    Validates the user's password.
    Requirements:
    - Must be at least 8 characters long
    - Must contain at least one uppercase letter
    - Must contain at least one lowercase letter
    - Must contain at least one digit
    
    Args:
        password (str): The password to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(password, str):
        return False
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True