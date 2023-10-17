if (usuariosValidos[usuario.value] && usuariosValidos[usuario.value] === contraseña.value) {
    // Las credenciales son válidas, enviar solicitud POST a la API
    fetch("http://127.0.0.1:8000/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            usuario: usuario.value,
            contraseña: contraseña.value
        })
    })
    .then(response => response.json())
    .then(data => {
        // Aquí puedes manejar la respuesta de la API, por ejemplo, redirigir al menú si el inicio de sesión fue exitoso.
        if (data.message === "Estudiante creado") {
            window.location.href = "../Menu/menu.html";
        } else {
            // Manejar errores de autenticación si es necesario
        }
    })
    .catch(error => {
        console.error("Error al enviar la solicitud a la API:", error);
    });
} else {
    // Las credenciales son incorrectas, muestra un mensaje de error
    mensajeError.innerText = "Usuario o contraseña incorrectos.";
    usuario.classList.add("campo-invalido");
    contraseña.classList.add("campo-invalido");
    mensajeError.classList.add("mensaje-error-visible");
}
