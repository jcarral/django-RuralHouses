// load jquery
var $ = require('jquery');

// load everything
require('jquery-ui');
var jQuery = $;

import navbar from './navbar.js';
navbar();

$(function() {
    $( "#id_nacimiento" ).datepicker({
            inline: true,
            showOtherMonths: true,
            dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        });

    $( "#draggable" ).draggable();

  });
