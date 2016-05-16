// load jquery
var $ = require('jquery');

// load everything
require('jquery-ui');

var jQuery = $;
require('./slide.js');
import navbar from './navbar.js';
import gestion_ajax from './gestion-ajax.js';
import registro from './registro.js';

navbar();
gestion_ajax();
registro();

$(function() {

  let dateInfo = {
          inline: true,
          showOtherMonths: true,
          dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
      };
  let offerBox = $( '#offer-container' );

    $( "#id_nacimiento" ).datepicker(dateInfo);
    $( "#busqueda_fechaInicio" ).datepicker(dateInfo);
    $( "#busqueda_fechaFin" ).datepicker(dateInfo);
    $( "#of-fechaFin" ).datepicker(dateInfo);
    $( "#of-fechaInicio" ).datepicker(dateInfo);
    $( "#offer-container" ).draggable();


    $( '#offer-close' ).on("click", ()=>{
      $(offerBox).fadeOut();
    });

    $( '#openofferbox' ).on('click', ()=>{
      $(offerBox).fadeIn();
    })
     $('.bxslider').bxSlider();
  });
