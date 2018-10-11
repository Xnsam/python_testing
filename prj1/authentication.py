"""Authentication Module."""


def login(username, password):
    try:
        users = ['george', 'bosco']
        if [username, password] in users:
            return True
        else:
            return False
    except Exception:
        print("Authentication Failed.")
        return False
