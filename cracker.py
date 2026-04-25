import hashlib
import itertools
import time


SUPPORTED_ALGOS = ['md5', 'sha1', 'sha256']


def hash_word(word, algo):
    """Hash a string using the specified algorithm."""
    if algo not in SUPPORTED_ALGOS:
        raise ValueError(f"Unsupported algorithm: {algo}")
    h = hashlib.new(algo)
    h.update(word.encode('utf-8'))
    return h.hexdigest()


def detect_algo(hash_value):
    """Auto-detect hash type based on length."""
    length_map = {
        32: 'md5',
        40: 'sha1',
        64: 'sha256'
    }
    return length_map.get(len(hash_value.strip()))


def dictionary_attack(target_hash, algo, wordlist_path):
    """Try every word in the wordlist."""
    start = time.time()
    attempts = 0
    target_hash = target_hash.lower().strip()

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                attempts += 1
                if hash_word(word, algo) == target_hash:
                    return {
                        'success': True,
                        'password': word,
                        'attempts': attempts,
                        'time': round(time.time() - start, 3),
                        'method': 'dictionary'
                    }
    except FileNotFoundError:
        return {
            'success': False,
            'error': f'Wordlist not found: {wordlist_path}',
            'attempts': 0,
            'time': 0
        }

    return {
        'success': False,
        'attempts': attempts,
        'time': round(time.time() - start, 3),
        'method': 'dictionary',
        'error': 'Password not found in wordlist'
    }


def brute_force_attack(target_hash, algo, charset, max_length, timeout=30):
    """Try every combination up to max_length."""
    start = time.time()
    attempts = 0
    target_hash = target_hash.lower().strip()

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            # Stop if timeout reached
            if time.time() - start > timeout:
                return {
                    'success': False,
                    'attempts': attempts,
                    'time': round(time.time() - start, 3),
                    'method': 'brute_force',
                    'error': f'Timeout reached ({timeout}s)'
                }

            word = ''.join(combo)
            attempts += 1
            if hash_word(word, algo) == target_hash:
                return {
                    'success': True,
                    'password': word,
                    'attempts': attempts,
                    'time': round(time.time() - start, 3),
                    'method': 'brute_force'
                }

    return {
        'success': False,
        'attempts': attempts,
        'time': round(time.time() - start, 3),
        'method': 'brute_force',
        'error': 'Password not found within given length/charset'
    }