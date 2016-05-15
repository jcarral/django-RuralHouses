var $ = require('jquery');
export default function gestion_ajax() {

  let $fechaInicio = $('#of-fechaInicio');
  let $fechaFin = $('#of-fechaFin');
  let $precio = $('#of-precio');


  let getCookie = (c_name) =>
    {
        if (document.cookie.length > 0)
        {
            let c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                let c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
     };

  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });

//EVENTOS para gestionar los formularios
  $("#favbtn").on("click", (event) =>{
    event.preventDefault();
    console.log("Favoritos click");
    crear_favorito();
    $("#favbtn").toggleClass('favorito-selected')
  });

  $( '#newOffer' ).on('click', (event) => {
    event.preventDefault();
    console.log("Creando oferta");
    crear_oferta();
  });

//Función para generar fechas en un formato que acepte el modelo
let formatDate = (date) => {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}

//Funcion auxiliar para crear oferats nuevas
  let crear_oferta = () => {
    let first = $($fechaInicio).val();
    first = formatDate(new Date(first));
    let last =  $($fechaFin).val();
    last = formatDate(new Date(last));
    let data = {
      'id': $('#newOffer').attr('data-idcasa'),
      'first': first,
      'last' : last,
      'precio' : $($precio).val()
    };
    console.log(data);
    $.ajax({
      url: '/nuevaoferta/',
      type: 'POST',
      data: data,
      success: (json) => {
        ofertaGuardada();
      },
      error: (xhr,errmsg,err)=>{
        console.log('Error');
        console.log(xhr);
      }
    });

  };

let ofertaGuardada = ()=>{
  let insert = `<div class="offer-item row"><p class="four columns"> ${$($fechaInicio).val()} </p> <p class="four columns">${$($fechaFin).val()} </p><p class="four columns"> ${$($precio).val()}</p></div>`;

  //Limpiado campos
  $($fechaInicio).val('');
  $($fechaFin).val('');
  $($precio).val('');

  $(insert).appendTo('#offer-list').hide().fadeIn(2000);
};
//Función auxiliar para crear favoritos
  let crear_favorito = ()=>{
    console.log("Creando favorito");
    let data = {
      'id': $('#favbtn').attr('data-idcasa')
    };

    $.ajax({
      url: '/fav/',
      type: 'POST',
      data: data,
      success: (json) => {
        console.log("Fav guardado");
        console.log(json);
      },
      error: (xhr,errmsg,err)=>{
        console.log('Error');
        console.log(xhr);
      }
    });

  };
}