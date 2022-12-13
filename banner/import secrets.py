import secrets

str(''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(20)))