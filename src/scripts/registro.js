var $ = require('jquery');

export default function registro() {
  //Global variables
  var validPassword = false;
  //Items cache
  var password = $("#txtNewPassword"),
    confirmPassword = $("#txtConfirmPassword"),
    form = $('#registerform'),
    username = $('#username'),
    email = $('#email'),
    firstname = $('#firstname');

  //Styles object
  var cssStyles = {
    error: {
      'border': '2px solid #e45858',
    },
    valid: {
      'border': '2px solid #66bd58',
    }
  };
  //Function to add new style to an item
  let addStyle = (item, styles) => {
    for (var st in styles)
      item.style[st] = styles[st];
  };

  //Function to check if the confirm password matches with the first,
  //any case, it adds new style to the input box
  let checkPasswordMatch = () => {
    let passwordVal = $(password).val();
    let confirmPasswordVal = $(confirmPassword).val();

    if (passwordVal != confirmPasswordVal) {
      addStyle(confirmPassword[0], cssStyles.error);
      validPassword = false;
    } else {
      addStyle(confirmPassword[0], cssStyles.valid);
      validPassword = true;
    }

  }

  //Function to check if the form is valid
  let validForm = (e) => {
    if ($(username).val().length == 0 || $(email).val().length == 0 || $(firstname).val().length == 0 || $(password).val().length == 0 || !validPassword) {
      e.preventDefault();
      alert("Faltan campos por rellenar en el formulario");
      return false;
    }
    return true;
  };

  $(confirmPassword).keyup(checkPasswordMatch);

  $(form).submit((event) => {
    validForm(event);
  });
};
