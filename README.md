# AES Encryption

A python aes encryption library

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install using pip

```sh
pip install aes-encryption
```

## Usage

```python
from aes_encryption import AESCipher

encryption_key: str = 'secret key'
cipher: AESCipher = AESCipher(encryption_key)  # this initializes the cipher with an encryption key
message: str = 'secret message'
encrypted: str = cipher.encrypt(message)  # this is how you encrypt your message
decrypted: str = cipher.decrypt(encrypted)  # this is how you decrypt your message
```


## Support

Please [open an issue](https://github.com/apinanyogaratnam/aes-encryption/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/aes-encryption/compare/).
