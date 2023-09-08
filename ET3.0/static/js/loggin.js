$(document).ready(function() {
    $('#containerforminico').submit(function(e) {
      var contraseña = $('#password').val();
      var email = $('#email').val();
     
  
      if (contraseña === '' || email === '' ) {
        e.preventDefault();
        alert('Por favor, complete todos los campos.');
      }
    });
  });

  