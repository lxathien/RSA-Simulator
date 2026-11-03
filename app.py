from flask import Flask, jsonify, render_template, request

from rsa import decrypt, encrypt, generate_keys

app = Flask(__name__)


# Trang chu
@app.route("/")
def home():
    return render_template("index.html")


# Tao khoa RSA
@app.route("/generate-keys", methods=["POST"])
def create_keys():
    public_key, private_key = generate_keys()

    return jsonify({
        "public_key": public_key,
        "private_key": private_key
    })


# Ma hoa
@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    data = request.json

    message = data["message"]
    public_key = tuple(data["public_key"])

    result = encrypt(message, public_key)

    return jsonify({"encrypted_message": result})


# Giai ma
@app.route("/decrypt", methods=["POST"])
def decrypt_message():
    data = request.json

    encrypted_message = data["encrypted_message"]
    private_key = tuple(data["private_key"])

    result = decrypt(encrypted_message, private_key)

    return jsonify({"decrypted_message": result})


if __name__ == "__main__":
    app.run(debug=True)
