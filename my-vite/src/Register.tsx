import { useState } from "react";

function Register() {
    const [form, setForm] = useState({
        email: "",
        username: "",
        password: "",
        phone: "",
    });

    const [errors, setErrors] = useState<any>({});

    const handleChange = (e: any) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: any) => {
        e.preventDefault();

        const res = await fetch(
            `${import.meta.env.VITE_API_URL}/register/`,
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(form),
            }
        );

        const data = await res.json();

        if (!res.ok) {
            setErrors(data);
        } else {
            alert("Реєстрація успішна 🎉");
            setErrors({});
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Реєстрація</h2>

            <input name="email" placeholder="Email" onChange={handleChange} />
            <input name="username" placeholder="Імʼя" onChange={handleChange} />
            <input name="phone" placeholder="+380XXXXXXXXX" onChange={handleChange} />
            <input
                name="password"
                type="password"
                placeholder="Пароль"
                onChange={handleChange}
            />

            {Object.keys(errors).map((key) => (
                <p key={key} style={{ color: "red" }}>
                    {errors[key]}
                </p>
            ))}

            <button>Зареєструватися</button>
        </form>
    );
}

export default Register;
