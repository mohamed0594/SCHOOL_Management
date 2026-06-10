
from models.auth_service import AuthService


auth = AuthService()


auth.login("admin@gmail.com", "1234")

if auth.verifier_role("admin"):
    print("Menu admin")