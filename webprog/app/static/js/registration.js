document.addEventListener("DOMContentLoaded", () => {
    const loginInput = document.getElementById("login");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");
    const submitButton = document.querySelector("button[type='submit']");
    const loginHint = document.createElement("div");
    const passwordHint = document.createElement("div");

    // Добавляем подсказки
    loginHint.classList.add("hint");
    passwordHint.classList.add("hint");
    loginInput.parentElement.appendChild(loginHint);
    passwordInput.parentElement.appendChild(passwordHint);

    // Проверки логина
    const validateLogin = () => {
        const login = loginInput.value;
        let errors = [];

        if (login.length < 3 || login.length > 16) {
            errors.push("Логин должен содержать от 3 до 16 символов.");
        }
        if (!/^[a-zA-Z0-9_]+$/.test(login)) {
            errors.push("Логин может содержать только латинские буквы, цифры и знак подчёркивания.");
        }

        // AJAX проверка на уникальность логина
        if (login.length >= 3 && login.length <= 16) {
            const xhr = new XMLHttpRequest();
            xhr.open("GET", `check_login.php?login=${login}`, true);
            xhr.onload = function() {
                if (xhr.status === 200) {
                    const response = xhr.responseText;
                    if (response === "exists") {
                        loginHint.className = "hint error";
                        loginHint.textContent = "Этот логин уже занят.";
                        submitButton.disabled = true;  // Деактивируем кнопку, если логин занят
                    } else {
                        loginHint.className = "hint success";
                        loginHint.textContent = "Логин доступен.";
                        submitButton.disabled = false;  // Активируем кнопку, если логин доступен
                    }
                }
            };
            xhr.send();
        }

        // Обновление подсказки
        if (errors.length) {
            loginHint.className = "hint error";
            loginHint.innerHTML = errors.map(err => `<li>${err}</li>`).join("");
        } else {
            loginHint.className = "hint success";
            loginHint.textContent = "Логин корректен.";
        }

        return errors.length === 0;
    };

    // Проверки пароля
    const validatePassword = () => {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        let errors = [];

        if (password.length < 8 || password.length > 32) {
            errors.push("Пароль должен содержать от 8 до 32 символов.");
        }
        if (!/[a-z]/.test(password)) {
            errors.push("Пароль должен содержать хотя бы одну строчную букву.");
        }
        if (!/[A-Z]/.test(password)) {
            errors.push("Пароль должен содержать хотя бы одну прописную букву.");
        }
        if (!/[0-9]/.test(password)) {
            errors.push("Пароль должен содержать хотя бы одну цифру.");
        }
        if (!/[!@#$%^&*_.,/|\\]/.test(password)) {
            errors.push("Пароль должен содержать хотя бы один специальный символ.");
        }
        if (password !== confirmPassword) {
            errors.push("Пароли не совпадают.");
        }

        // Обновление подсказки
        if (errors.length) {
            passwordHint.className = "hint error";
            passwordHint.innerHTML = errors.map(err => `<li>${err}</li>`).join("");
        } else {
            passwordHint.className = "hint success";
            passwordHint.textContent = "Пароль корректен.";
        }

        return errors.length === 0;
    };

    // Проверка всех полей
    const validateForm = () => {
        const isLoginValid = validateLogin();
        const isPasswordValid = validatePassword();
        submitButton.disabled = !(isLoginValid && isPasswordValid);
    };

    // События ввода
    loginInput.addEventListener("input", validateForm);
    passwordInput.addEventListener("input", validateForm);
    confirmPasswordInput.addEventListener("input", validateForm);
});
