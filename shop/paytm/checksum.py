
import base64
import string
import random
import hashlib
from Crypto.Cipher import AES

IV = "@@@@&&&&####$$$$"

BLOCK_SIZE = 16


def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + chr(length) * length


def unpad(data):
    return data[:-ord(data[len(data) - 1:])]


def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def __get_param_string__(params):
    params_string = []
    for key in sorted(params.keys()):
        if params[key] == "null":
            params_string.append('')
        else:
            params_string.append(str(params[key]))
    return '|'.join(params_string)


def __calculate_checksum__(param_string, salt, key):
    final_string = param_string + '|' + salt
    hash_string = hashlib.sha256(final_string.encode()).hexdigest() + salt
    return __encode__(hash_string, key)


def generate_checksum(param_dict, key):
    salt = __id_generator__(4)
    param_string = __get_param_string__(param_dict)
    return __calculate_checksum__(param_string, salt, key)


def verify_checksum(param_dict, key, checksum):
    param_string = __get_param_string__(param_dict)
    salt = checksum[-4:]
    calculated_checksum = __calculate_checksum__(param_string, salt, key)
    return calculated_checksum == checksum


def __encode__(data, key):
    key = key.encode('utf-8')
    data = pad(data).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, IV.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(data)).decode("utf-8")


def __decode__(data, key):
    key = key.encode('utf-8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_CBC, IV.encode('utf-8'))
    return unpad(cipher.decrypt(data)).decode('utf-8')