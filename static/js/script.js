let publicKey = null;
let privateKey = null;
let encryptedMessage = null;

// Tao khoa RSA
document.getElementById("generateButton").addEventListener("click", async function () {
    try {
        const response = await fetch("/generate-keys", {
            method: "POST"
        });

        const data = await response.json();

        publicKey = data.public_key;
        privateKey = data.private_key;

        document.getElementById("publicKey").value = JSON.stringify(publicKey);
        document.getElementById("privateKey").value = JSON.stringify(privateKey);

        encryptedMessage = null;
        document.getElementById("encryptedMessage").value = "";
        document.getElementById("decryptedMessage").value = "";

        document.getElementById("status").textContent = "Tạo khóa thành công!";
    } catch (error) {
        document.getElementById("status").textContent = "Không thể tạo khóa. Vui lòng thử lại.";
    }
});

// Ma hoa thong diep
document.getElementById("encryptButton").addEventListener("click", async function () {
    if (publicKey === null) {
        document.getElementById("status").textContent = "Vui lòng tạo khóa trước!";
        return;
    }

    if (document.getElementById("message").value === "") {
        document.getElementById("status").textContent = "Vui lòng nhập thông điệp cần mã hóa!";
        return;
    }

    try {
        const response = await fetch("/encrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: document.getElementById("message").value,
                public_key: publicKey
            })
        });

        const data = await response.json();

        if (!response.ok) {
            document.getElementById("status").textContent = data.error;
            return;
        }

        encryptedMessage = data.encrypted_message;
        document.getElementById("encryptedMessage").value = JSON.stringify(encryptedMessage);
        document.getElementById("decryptedMessage").value = "";
        document.getElementById("status").textContent = "Mã hóa thành công!";
    } catch (error) {
        document.getElementById("status").textContent = "Có lỗi xảy ra khi mã hóa.";
    }
});

// Giai ma thong diep
document.getElementById("decryptButton").addEventListener("click", async function () {
    if (privateKey === null) {
        document.getElementById("status").textContent = "Vui lòng tạo khóa trước!";
        return;
    }

    if (encryptedMessage === null) {
        document.getElementById("status").textContent = "Vui lòng mã hóa thông điệp trước!";
        return;
    }

    try {
        const response = await fetch("/decrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                encrypted_message: encryptedMessage,
                private_key: privateKey
            })
        });

        const data = await response.json();

        if (!response.ok) {
            document.getElementById("status").textContent = data.error;
            return;
        }

        document.getElementById("decryptedMessage").value = data.decrypted_message;
        document.getElementById("status").textContent = "Giải mã thành công!";
    } catch (error) {
        document.getElementById("status").textContent = "Có lỗi xảy ra khi giải mã.";
    }
});
