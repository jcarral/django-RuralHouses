// load jquery
var $ = require('jquery');

// load everything
require('jquery-ui');

var jQuery = $;
require('./slide.js');
import navbar from './navbar.js';
import gestion_ajax from './gestion-ajax.js';
import registro from './registro.js';
import TeleportAutocomplete from './autocomplete.js';

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

    $( '#min-precio' ).on("change mousemove", ()=>{
      $( '#precio-minimo' ).text($( '#min-precio' ).val());
    });
    $( '#max-precio' ).on("change mousemove", ()=>{
      $( '#precio-maximo' ).text($( '#max-precio' ).val());
    });

     $('.bxslider').bxSlider();


    $("#searchform").submit(function(){
        $("input").each(function(index, obj){
            if($(obj).val() == "") {
                $(obj).remove();
            }
        });
        if($('#use-price').is(':checked')){
          $('#max-precio').remove();
          $('#min-precio').remove();
        }
        $('#use-price').remove();
    });

     var $results = document.querySelector('.results');
      var appendToResult = $results.insertAdjacentHTML.bind($results, 'afterend');
      TeleportAutocomplete.init('.city-input').on('change', function(value) {
        appendToResult('<pre class="hidden">' + JSON.stringify(value, null, 2) + '</pre>');
      });
  });
