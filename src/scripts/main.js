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

  });
