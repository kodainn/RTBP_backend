import hashlib

def create_hash_password(plaintext_password: str) -> str:
    return hashlib.sha256(plaintext_password.encode()).hexdigest()


def vertify_password(hash_password: str, plaintext_password: str) -> bool:
    if hashlib.sha256(plaintext_password.encode()).hexdigest() != hash_password:
        return False
    
    return True