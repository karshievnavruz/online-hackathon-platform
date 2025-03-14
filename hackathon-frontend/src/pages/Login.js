import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/token/", {
        username,
        password,
      });
      localStorage.setItem("access_token", response.data.access);
      alert("Login muvaffaqiyatli!");
    } catch (error) {
      alert("Xatolik yuz berdi!");
    }
  };

  return (
    <div>
      <h2>Kirish</h2>
      <form onSubmit={handleLogin}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Parol" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Kirish</button>
      </form>
    </div>
  );
};

export default Login;
