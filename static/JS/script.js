javascript
$(document).ready(function() {
    $('#login-form').on('submit', function(e) {
        e.preventDefault(); // Evita que el formulario se envíe de la forma predeterminada

        $.ajax({
            url: '/registro', // La URL a la que se enviarán los datos del formulario
            type: 'POST',
            data: $(this).serialize(), // Serializa los datos del formulario
            success: function(response) {
                // Si la solicitud es exitosa, puedes redirigir al usuario al menu
                window.location.href = '/login.html';
            },
            error: function(xhr, status, error) {
                // Si ocurre un error, muestra el mensaje de error en el contenedor
                $('#error-message').text('Error: ' + xhr.responseText);
            }
        });
    });
});