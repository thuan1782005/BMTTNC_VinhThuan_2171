from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher  
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

# ==========================================
# ROUTER FOR HOME PAGE
# ==========================================
@app.route("/")
def home():
    return render_template('index.html')


# ==========================================
# ROUTER FOR CAESAR CIPHER
# ==========================================
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    if request.is_json:
        data = request.get_json()
        text = data.get('plain_text', '')
        key = int(data.get('key', 0))
    else:
        text = request.form.get('inputPlainText', '')
        key = int(request.form.get('inputKeyPlain', 0))
        
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    
    # Trả về JSON để hiển thị trực tiếp lên màn hình qua AJAX
    return jsonify({'result': encrypted_text, 'encrypted_text': encrypted_text})

@app.route("/decrypt", methods=['POST'])
@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    if request.is_json:
        data = request.get_json()
        text = data.get('cipher_text', '')
        key = int(data.get('key', 0))
    else:
        text = request.form.get('inputCipherText', '')
        key = int(request.form.get('inputKeyCipher', 0))
        
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    
    return jsonify({'result': decrypted_text, 'cipher_text': decrypted_text})


# ==========================================
# ROUTER FOR VIGENERE CIPHER
# ==========================================
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt_route():
    if request.is_json:
        data = request.get_json()
        text = data.get('plain_text', '')
        key = data.get('key', '')
    else:
        text = request.form.get('inputPlaintext', '')
        key = request.form.get('inputKeyPlain', '')
        
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key) 
    
    return jsonify({'result': encrypted_text, 'encrypted_text': encrypted_text})

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt_route():
    if request.is_json:
        data = request.get_json()
        text = data.get('cipher_text', '')
        key = data.get('key', '')
    else:
        text = request.form.get('inputCipherText', '')
        key = request.form.get('inputKeyCipher', '')
        
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.vigenere_decrypt(encrypted_text=text, key=key) 
    
    return jsonify({'result': decrypted_text, 'decrypted_text': decrypted_text})


# ==========================================
# ROUTER FOR RAIL FENCE CIPHER
# ==========================================
@app.route("/railfence")
def railfence_page():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt_route():
    if request.is_json:
        data = request.get_json()
        text = data.get('plain_text', '')
        key = int(data.get('key', 1))
    else:
        text = request.form.get('inputPlaintext', '')
        key = int(request.form.get('inputKeyPlain', 1))
        
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(plain_text=text, num_rails=key) 
    
    return jsonify({'result': encrypted_text, 'encrypted_text': encrypted_text})

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt_route():
    if request.is_json:
        data = request.get_json()
        text = data.get('cipher_text', '')
        key = int(data.get('key', 1))
    else:
        text = request.form.get('inputCipherText', '')
        key = int(request.form.get('inputKeyCipher', 1))
        
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(cipher_text=text, num_rails=key) 
    
    return jsonify({'result': decrypted_text, 'decrypted_text': decrypted_text})


# ==========================================
# ROUTER FOR PLAYFAIR CIPHER
# ==========================================
@app.route("/playfair")
def playfair_page():
    return render_template('playfair.html')

@app.route("/api/playfair/creatematrix", methods=['POST'])
def playfair_matrix():
    if request.is_json:
        data = request.get_json()
        key = data.get('key', '')
    else:
        key = request.form.get('key') or request.form.get('inputKeyPlain') or request.form.get('inputKeyWord') or ''
        
    if not key:
        return jsonify({'error': 'Key không được để trống'}), 400
        
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    return jsonify(matrix)

@app.route("/playfair/encrypt", methods=['POST'])
@app.route("/api/playfair/encrypt", methods=['POST'])
def playfair_encrypt_route():
    if request.is_json or request.path.startswith('/api/'):
        data = request.get_json()
        text = data.get('plain_text', '')
        key = data.get('key', '')
    else:
        text = request.form.get('inputPlaintext', '')
        key = request.form.get('inputKeyPlain', '')
        
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    
    return jsonify({'result': encrypted_text, 'encrypted_text': encrypted_text})

@app.route("/playfair/decrypt", methods=['POST'])
@app.route("/api/playfair/decrypt", methods=['POST'])
def playfair_decrypt_route():
    if request.is_json or request.path.startswith('/api/'):
        data = request.get_json()
        text = data.get('cipher_text', '')
        key = data.get('key', '')
    else:
        text = request.form.get('inputCipherText', '')
        key = request.form.get('inputKeyWord', '')  # Sửa đồng bộ lỗi KeyError inputKeyCipher từ bài trước
        
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    
    return jsonify({'result': decrypted_text, 'cipher_text': decrypted_text})


# ==========================================
# ROUTER FOR TRANSPOSITION CIPHER
# ==========================================
@app.route("/transposition")
def transposition_page():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
@app.route("/api/transposition/encrypt", methods=['POST'])
def transposition_encrypt_route():
    if request.is_json or request.path.startswith('/api/'):
        data = request.get_json()
        text = data.get('plain_text', '')
        key = int(data.get('key', 1))
    else:
        text = request.form.get('inputPlaintext', '')
        key = int(request.form.get('inputKeyPlain', 1))
        
    trans_cipher = TranspositionCipher()
    encrypted_text = trans_cipher.encrypt(text, key)
    
    return jsonify({'result': encrypted_text, 'encrypted_text': encrypted_text})

@app.route("/transposition/decrypt", methods=['POST'])
@app.route("/api/transposition/decrypt", methods=['POST'])
def transposition_decrypt_route():
    if request.is_json or request.path.startswith('/api/'):
        data = request.get_json()
        text = data.get('cipher_text', '')
        key = int(data.get('key', 1))
    else:
        text = request.form.get('inputCipherText', '')
        key = int(request.form.get('inputKeyCipher', 1))
        
    trans_cipher = TranspositionCipher()
    decrypted_text = trans_cipher.decrypt(text, key)
    
    return jsonify({'result': decrypted_text, 'cipher_text': decrypted_text})


# Main Function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)