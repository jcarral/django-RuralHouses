// load jquery
var $ = require('jquery');

// load everything
require('jquery-ui');
var jQuery = $;

import navbar from './navbar.js';
navbar();

$(function() {

  let dateInfo = {
          inline: true,
          showOtherMonths: true,
          dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      };

    $( "#id_nacimiento" ).datepicker(dateInfo);
    $( "#busqueda_fechaInicio" ).datepicker(dateInfo);
    $( "#busqueda_fechaFin" ).datepicker(dateInfo);

    $( "#draggable" ).draggable();

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

    $("#favbtn").on("click", (event) =>{
      event.preventDefault();
      console.log("Favoritos click");
      crear_favorito();
    });

    let crear_favorito = ()=>{
      console.log("Creando favorito");
      let data = {
        'id': $('#favbtn').attr('data-idcasa'),
        'csrfmiddlewaretoken': $('#csrf').val()
      };
      console.log(data);

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


  });
