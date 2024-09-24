import hashlib
import os
import glob


def write_hash_to_file(hash_value):
    existing_files = glob.glob('giaTriBam*.txt')
    new_file_name = f'giaTriBam{len(existing_files) + 1}.txt'
    with open(new_file_name, 'w') as f:
        f.write(hash_value + '\n')


def sha1_hash(input_string):
    sha1 = hashlib.sha1()
    sha1.update(input_string.encode('utf-8'))
    hashed_value = sha1.hexdigest()
    write_hash_to_file(hashed_value)
    return hashed_value


def calculate_file_hash(file_path, write_to_file=True):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha1.update(data)
    hashed_value = sha1.hexdigest()
    if write_to_file:
        write_hash_to_file(hashed_value)
    return hashed_value


def compare_hashes(hash1, hash2):
    return hash1 == hash2
