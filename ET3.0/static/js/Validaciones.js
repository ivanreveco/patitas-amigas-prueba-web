 


$(document).ready(function Validaciones() {
  

  $('#formulario').submit(function largos_nombres(event) {//validacion de largo de nombre y apellido 
    var nombre = $('#nombre').val();
    var apellido = $('#apellido').val();

    if (nombre.length < 3 || nombre.length > 30) {
      $('#error-nombre').text('El nombre debe tener entre 3 y 30 caracteres').show();
      event.preventDefault();
      
    } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(nombre)) {
      $('#error-nombre').text('El nombre solo puede contener letras y espacios').show();
      event.preventDefault();
     
    } else {
      $('#error-nombre').hide();
      
    }
       // El formulario es válido
      if (apellido.length < 3 || apellido.length > 30) {
        $('#error-apellido').text('El apellido debe tener entre 3 y 30 caracteres').show();
        event.preventDefault();

       // El formulario no es válido
      } else if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(apellido)) {
        $('#error-apellido').text('El apellido solo puede contener letras y espacios').show();
        event.preventDefault();
       
      } else {
        $('#error-apellido').hide();
         // El formular
       
      }
     
    });//fin validacion de largo de nombre y apellido
  
  $('#formulario').submit(function validacion_correo(event) {//bloque para validar que el correo tenga un dominio correcto
    
    var correo = $('#email').val();

    if (correo.length <3){
      $("#error-correo").text("favor ingresar correo").show();
      event.preventDefault(); // Evita que se envíe el formulario
      
    }else if (correo.endsWith("@yahoo.com") || correo.endsWith("@hotmail.com") || correo.endsWith("@outlook.com")|| correo.endsWith("@gmail.com")){
      $("#error-correo").hide()
      
    }else{
     
      $("#error-correo").text("El dominio de correo no es reconocido favor usar yahoo,hotmail,gmail,outlook .com").show();
      event.preventDefault(); // Evita que se envíe el formulario
      
    }
  });//bloque para validar que el correo tenga un dominio correcto
  $("#formulario").submit(function validacion_edad(event){//bloque para validar que sea mayor de edad
   
    var edad = $("#edad").val();

    if(edad >= 18){
      $("#error-edad").hide();
    
     
    }else{
      $("#error-edad").text("Debes ser mayor de edad para registrarte").show();
      event.preventDefault(); // Evita que se envíe el formulario
      
    }


  });// fin bloque para validar que sea mayor de edad
  $("#formulario").submit(function validar_contraseña(event){//bloque para validar si la contraseña es correcta
    
    var contraseña =$("#password").val();
    var mayusculas =/[A-Z]/;

    if(contraseña.length<8){
      $("#error-contraseña").text("La contraseña debe contener 8 caracteres").show();
      event.preventDefault();
      
    }else if(!mayusculas.test(contraseña)){
      $("#error-contraseña").text("La contraseña debe contener al menos una mayuscula").show();
      event.preventDefault();
      
    }else{
      $("#error-contraseña").hide();
      
    }
  });// fin bloque para validar si la contraseña es correcta
  $("#formulario").submit(function confirmar_contraseña(event){// bloque para confirmar que las contraseñas sean iguales
    

    var contraseña = $("#password").val();
    var conficontraseña = $("#repassword").val();

    if(contraseña!== conficontraseña){
      $("#error-repassword").text("Las contraseña no coinciden").show();
      event.preventDefault();
      
    }else{
      $("#error-repassword").hide();
      
    
    }

    
  });// fin bloque para confirmar que las contraseñas sean iguales
  $("#formulario").submit(function validar_checkbox(event){
   
    
    var check = $("#aceptar").prop("checked");
    if (check){
      $("#error-check").hide();
      $("#formulario").submit();
      
      
      
    }else{
      $("#error-check").text("favor aceptar terminos").show()
      $("reg-exi").hide()
      event.preventDefault();
      
    }
  });//fin bloque validacion check boxs
  
});
 


 

  
