import { useState } from "react";

function Register() {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        const response = await fetch(
            `${import.meta.env.VITE_API_URL}/register/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email: email,
                    username: username,
                    password: password,
                }),
            }
        );

        const data = await response.json();
        alert(data.message || "Помилка");
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Реєстрація</h2>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />

            <input
                type="text"
                placeholder="Ім'я користувача"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
            />

            <input
                type="password"
                placeholder="Пароль"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />

            <button type="submit">Зареєструватися</button>
        </form>
    );
}

export default Register;
