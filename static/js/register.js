$(document)
.ready(function() {
  $('.ui.register.form')
    .form({
      fields: {
        email: {
          identifier: 'email',
          rules: [
            {
              type   : 'regExp',
              value : /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            }
          ]
        },
        password1: {
          identifier: 'password1',
          rules: [
            {
              type   : 'minLength[8]',
              prompt : 'The passwords should be longer than 8 characters'
            },
            {
              type   : 'empty',
              prompt : 'Please enter a password'
            }
          ]
        },
        password2: {
          identifier: 'password2',
          rules: [
            {
              type   : 'match[password1]',
              prompt : 'The passwords should be same'
            }
          ]
        },
        first_name: {
          identifier: 'first_name',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter your first_name'
            }
          ]
        },
        name: {
          identifier: 'last_name',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter your last_name'
            }
          ]
        },
        phone_number: {
          identifier: 'phone_number',
          rules: [
            {
              type   : 'regExp',
              value : /^\d{3}-\d{3,4}-\d{4}$/
            }
          ]
        },
      },
    });
});