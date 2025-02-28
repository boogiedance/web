document.addEventListener("DOMContentLoaded", () => {
    const loginInput = document.getElementById("login");
    const passwordInput = document.getElementById("password");
    const submitButton = document.querySelector("button[type='submit']");

    // Проверка логина
    const validateLogin = () => {
        const login = loginInput.value;
        return login.length >= 3;  // Минимальная длина логина 3 символа
    };

    // Проверка пароля
    const validatePassword = () => {
        const password = passwordInput.value;
        return password.length >= 8;  // Минимальная длина пароля 8 символов
    };

    // Проверка всех полей
    const validateForm = () => {
        const isLoginValid = validateLogin();
        const isPasswordValid = validatePassword();
        submitButton.disabled = !(isLoginValid && isPasswordValid); // Если форма не валидна, кнопка остается заблокированной
    };

    // События ввода
    loginInput.addEventListener("input", validateForm);
    passwordInput.addEventListener("input", validateForm);

    // Изначальная проверка при загрузке страницы
    validateForm();
});
