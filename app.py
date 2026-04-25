from flask import Flask, render_template, request, jsonify
from cracker import (
    dictionary_attack,
    brute_force_attack,
    detect_algo,
    hash_word,
    SUPPORTED_ALGOS
)
import string
import os

app = Flask(__name__)

# Configuration
WORDLIST_PATH = os.path.join('wordlists', 'rockyou-small.txt')
BRUTE_FORCE_TIMEOUT = 30  # seconds


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hash', methods=['POST'])
def make_hash():
    """Generate a hash for testing purposes."""
    data = request.get_json()
    word = data.get('word', '')
    algo = data.get('algo', 'md5').lower()

    if not word:
        return jsonify({'error': 'No input provided'}), 400

    if algo not in SUPPORTED_ALGOS:
        return jsonify({'error': f'Unsupported algorithm: {algo}'}), 400

    return jsonify({
        'hash': hash_word(word, algo),
        'algo': algo
    })


@app.route('/crack', methods=['POST'])
def crack():
    """Crack a hash using dictionary or brute force."""
    data = request.get_json()
    target_hash = data.get('hash', '').strip()

    if not target_hash:
        return jsonify({'success': False, 'error': 'No hash provided'}), 400

    # Auto-detect or use provided algorithm
    algo = data.get('algo') or detect_algo(target_hash)
    if not algo:
        return jsonify({
            'success': False,
            'error': 'Could not detect hash type. Please specify manually.'
        }), 400

    method = data.get('method', 'dictionary')

    # Dictionary attack
    if method == 'dictionary':
        result = dictionary_attack(target_hash, algo, WORDLIST_PATH)

    # Brute force attack
    elif method == 'brute':
        charset_type = data.get('charset', 'lower')
        charset_map = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits,
            'alnum': string.ascii_letters + string.digits,
            'all': string.ascii_letters + string.digits + string.punctuation
        }
        charset = charset_map.get(charset_type, string.ascii_lowercase)

        try:
            max_length = int(data.get('max_length', 4))
            if max_length < 1 or max_length > 8:
                return jsonify({
                    'success': False,
                    'error': 'max_length must be between 1 and 8'
                }), 400
        except ValueError:
            return jsonify({'success': False, 'error': 'Invalid max_length'}), 400

        result = brute_force_attack(
            target_hash, algo, charset, max_length, timeout=BRUTE_FORCE_TIMEOUT
        )
    else:
        return jsonify({'success': False, 'error': 'Invalid method'}), 400

    result['algo'] = algo
    return jsonify(result)


if __name__ == '__main__':
    # Make sure required folders exist
    os.makedirs('wordlists', exist_ok=True)
    app.run(debug=True, host='127.0.0.1', port=5000)