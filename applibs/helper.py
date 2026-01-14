import hmac
import ulid
import hashlib

from django.conf import settings

def generate_unique_token_for_url() -> str:
    token = str(ulid.new())
    return token[10:]

def generate_hashed_token(data: str) -> str:
    hash_key = settings.TOKEN_HASH_KEY
    
    encoded_data = data.encode('utf-8')
    encoded_hash_key = hash_key.encode('utf-8')

    return hmac.new(encoded_hash_key, encoded_data, hashlib.sha256).hexdigest()