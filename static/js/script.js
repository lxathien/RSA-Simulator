let publicKey = null;
let privateKey = null;
let encryptedMessage = null;

const generateButton = document.getElementById("generateButton");
const encryptButton = document.getElementById("encryptButton");
const decryptButton = document.getElementById("decryptButton");
const statusText = document.getElementById("status");


// Tao khoa RSA
generateButton.addEventListener("click", async function () {
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

        statusText.textContent = "Tạo khóa thành công!";
    } catch (error) {
        statusText.textContent = "Không thể tạo khóa. Vui lòng thử lại.";
    }
});


// Ma hoa thong diep
encryptButton.addEventListener("click", async function () {
    const message = document.getElementById("message").value;

    if (publicKey === null) {
        statusText.textContent = "Vui lòng tạo khóa trước!";
        return;
    }

    if (message === "") {
        statusText.textContent = "Vui lòng nhập thông điệp cần mã hóa!";
        return;
    }

    try {
        const response = await fetch("/encrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                public_key: publicKey
            })
        });

        const data = await response.json();

        if (!response.ok) {
            statusText.textContent = data.error;
            return;
        }

        encryptedMessage = data.encrypted_message;
        document.getElementById("encryptedMessage").value =
            JSON.stringify(encryptedMessage);

        document.getElementById("decryptedMessage").value = "";
        statusText.textContent = "Mã hóa thành công!";
    } catch (error) {
        statusText.textContent = "Có lỗi xảy ra khi mã hóa.";
    }
});


// Giai ma thong diep
decryptButton.addEventListener("click", async function () {
    if (privateKey === null) {
        statusText.textContent = "Vui lòng tạo khóa trước!";
        return;
    }

    if (encryptedMessage === null) {
        statusText.textContent = "Vui lòng mã hóa thông điệp trước!";
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
            statusText.textContent = data.error;
            return;
        }

        document.getElementById("decryptedMessage").value =
            data.decrypted_message;

        statusText.textContent = "Giải mã thành công!";
    } catch (error) {
        statusText.textContent = "Có lỗi xảy ra khi giải mã.";
    }
});
