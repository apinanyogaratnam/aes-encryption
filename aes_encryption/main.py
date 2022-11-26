import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self: "AESCipher", key: str) -> None:
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self: "AESCipher", raw: str) -> str:
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode("utf-8")

    def decrypt(self: "AESCipher", enc: bytes) -> str:
        enc = base64.b64decode(enc)
        iv = enc[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size :])).decode("utf-8")

    def _pad(self: "AESCipher", s: str) -> str:
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s: str) -> str:
        return s[: -ord(s[len(s) - 1 :])]


if __name__ == "__main__":
    cipher = AESCipher("secret key")
    encrypted = cipher.encrypt("secret message")
    decrypted = cipher.decrypt(encrypted)
    print(encrypted)
    print(decrypted)
