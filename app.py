from flask import Flask, render_template, request, jsonify
from rsa import generate_keys, encrypt, decrypt

app = Flask(__name__)


# Hien thi trang chu
@app.route("/")
def home():
    return render_template("index.html")


# Tao public key va private key
@app.route("/generate-keys", methods=["POST"])
def create_keys():
    public_key, private_key = generate_keys()

    return jsonify({
        "public_key": public_key,
        "private_key": private_key
    })


# Ma hoa thong diep
@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    data = request.get_json()

    message = data.get("message")
    public_key = data.get("public_key")

    if not message or not public_key:
        return jsonify({"error": "Vui long nhap thong diep va public key"}), 400

    try:
        public_key = tuple(public_key)
        encrypted_message = encrypt(message, public_key)

        return jsonify({
            "encrypted_message": encrypted_message
        })

    except Exception as error:
        return jsonify({"error": str(error)}), 400


# Giai ma thong diep
@app.route("/decrypt", methods=["POST"])
def decrypt_message():
    data = request.get_json()

    encrypted_message = data.get("encrypted_message")
    private_key = data.get("private_key")

    if encrypted_message is None or not private_key:
        return jsonify({"error": "Vui long nhap ban ma va private key"}), 400

    try:
        private_key = tuple(private_key)
        decrypted_message = decrypt(encrypted_message, private_key)

        return jsonify({
            "decrypted_message": decrypted_message
        })

    except Exception as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(debug=True)
