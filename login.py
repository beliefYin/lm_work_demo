from passlib.context import CryptContext

pwd_context = CryptContext(
	schemes=["pbkdf2_sha256"],
	default="pbkdf2_sha256",
	pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
	return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
	return pwd_context.verify(password, hashed)

class Login():
	def __init__(self, root=None):
		self.create_page(root)

	def create_page(self, root=None):
		self.root = root
		self.root.geometry('800x600')








# password = "123"

# hashed = encrypt_password(password)
# print("hashed:%s"%hashed)
# print(check_encrypted_password("dd", hashed))