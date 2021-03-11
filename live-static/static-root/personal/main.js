//creado manualmente para globalizar los js
var $ = jQuery.noConflict();

//funciones para abrir modales
function abrir_modal_agregar(url){
$('#modalAgregar').load(url, function(){
  $(this).modal('show');
});
}

function abrir_modal_editar(url){
$('#modalEditar').load(url, function(){
  $(this).modal('show');
});
}

function abrir_modal_eliminar(url){
$('#modalEliminar').load(url, function(){
  $(this).modal('show');
});
}
function abrir_modal_detalles(url){
$('#modalDetalles').load(url, function(){
  $(this).modal('show');
});
}
function abrir_modal_reservar(url){
$('#modalReservar').load(url, function(){
  $(this).modal('show');
});
}
//funciones para cerrar modales
function cerrar_modal_agregar(){
	$('#modalAgregar').modal('hide');
}
function cerrar_modal_detalles(){
	$('#modalDetalles').modal('hide');
}
function cerrar_modal_editar(){
	$('#modalEditar').modal('hide');
}
function cerrar_modales_editar(){
	$('#modalEditar').modal('hide');
	cerrar_modal_detalles();
}
function cerrar_modal_eliminar(){
	$('#modalEliminar').modal('hide');
}

//funcion para bloquear button de agregar cuando este creando uno neuvo
function bloquearButton(){
	if($('#bloquear_button_agregar').prop('disabled')){
		$('#bloquear_button_agregar').prop('disabled',false);
	}else{
		$('#bloquear_button_agregar').prop('disabled',true);
	}
}

//Funcion para mostrar errores
//esta funcion mostrarErroresAgregar() es llamda desde templates.js
function mostrarErroresAgregar(errores){
	//erroresAgregar es un id que es llamado de perfil_ModalEditarUsuario.html
	$('#erroresAgregar').html("");
	let error = "";
	//if ($("input").next('p').length) $("input").nextAll('p').empty();
	for(let item in errores.responseJSON.error){
	    for (var i in errores.responseJSON.error[item]) {
	      // object message error django
	      var $input = $("input[name='"+ item +"']");
	      $input.before('<div class = "alert alert-danger alert-dismissible fade show" ><button type="button" class="close" data-dismiss="alert">&times;</button><strong>Oops! </strong>' + errores.responseJSON.error[item][i] + '</div>');
	    }
		 
	}
	$('#erroresAgregar').append(error);
}

function mostrarErroresEditar(errores){
	//erroresEditar es un id que es llamado de perfil_ModalEditarUsuario.html
	$('#erroresEditar').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
	    for (var i in errores.responseJSON.error[item]) {
	      // object message error django
	      var $input = $("input[name='"+ item +"']");
	      $input.before('<div class = "alert alert-danger alert-dismissible fade show" ><button type="button" class="close" data-dismiss="alert">&times;</button><strong>Oops! </strong>' + errores.responseJSON.error[item][i] + '</div>');
	    }
		 
	}
	$('#erroresEditar').append(error);
}


//funciones para sweet alert
//estas funciones son llamdas cuando agan la peticion
//es decir son llamadas desde templates.js
function sweetError(mensaje){
	//Swal.fire()-> es la manera para crear una instancia para sweet alert
	Swal.fire({
		title: 'Lo sentimos!',
		text: mensaje,
		icon: 'error'
	})
}
function sweetSuccess(mensaje){
	//Swal.fire()-> es la manera para crear una instancia para sweet alert
	Swal.fire({
		title: 'Felicidades!',
		text: mensaje,
		icon: 'success'
	})
}

//para obtener el csrftoken desde archivos js
function getCookie(name) { 
    var cookieValue = null; 
    if (document.cookie && document.cookie !== '') { 
     var cookies = document.cookie.split(';'); 
     for (var i = 0; i < cookies.length; i++) { 
      var cookie = jQuery.trim(cookies[i]); 
      // Does this cookie string begin with the name we want? 
      if (cookie.substring(0, name.length + 1) === (name + '=')) { 
       cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); 
       break; 
      } 
     } 
    } 
    return cookieValue; 
} 
