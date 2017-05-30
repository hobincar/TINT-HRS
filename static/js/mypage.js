$(document)
    .ready(function() {
        $('.menu .item').tab();
        $('.ui.modal').modal();
        $('.ui.dropdown').dropdown();

        $(".modal-close-btn").on('click', () => $(".ui.modal").modal('hide'));

        $.fn.form.settings.rules.greaterThan = function (inputValue, validationValue) {
           let operand = $(`input[name=${validationValue}]`).val();
           return inputValue > operand;
        };
        $('.ui.modify.form')
            .form({
                fields: {
                    check_in: {
                        identifier: 'check_in',
                        rules: [{
                            type : 'regExp',
                            value: /\d{4}-\d{2}-\d{2}/
                        },]
                    },
                check_out: {
                  identifier: 'check_out',
                  rules: [
                    {
                        type : 'regExp',
                        value: /\d{4}-\d{2}-\d{2}/
                    },
                    {
                        type: 'greaterThan[check_in]',
                        prompt: 'check-out date should be later than check-in'
                    }
                  ]
                },
                n_adult: {
                  identifier: 'n_adult',
                  rules: [
                    {
                      type   : 'empty',
                      prompt : 'Please enter the old password'
                    },
                  ]
                },
                n_child: {
                  identifier: 'n_child',
                  rules: [
                    {
                      type   : 'empty',
                      prompt : 'Please enter the old password'
                    },
                  ]
                },
                n_breakfast: {
                  identifier: 'n_breakfast',
                  rules: [
                    {
                      type   : 'empty',
                      prompt : 'Please enter the old password'
                    },
                  ]
                },
                n_baby_bed: {
                  identifier: 'n_baby_bed',
                  rules: [
                    {
                      type   : 'empty',
                      prompt : 'Please enter the old password'
                    },
                  ]
                },
              },
              onSuccess: function(event) {
                event.preventDefault();
                progressPayModal();
                setTimeout(() => $(this).unbind(event).submit(), 2000);
              },
            });
        $('.ui.pay.form')
            .form({
              fields: {
                card_type: {
                  identifier: 'card_type',
                  rules: [
                    {
                      type: 'empty',
                      prompt: 'Please select card type'
                    }
                  ]
                },
                card_number: {
                  identifier: 'card_number',
                  rules: [
                    {
                      type : 'regExp',
                      value: /\d{16}/
                    }
                  ]
                },
                card_cvc: {
                  identifier: 'card_cvc',
                  rules: [
                    {
                      type: 'regExp',
                      value: /\d{3}/
                    }
                  ]
                },
                card_expire_month: {
                  identifier: 'card_expire_month',
                  rules: [
                    {
                      type: 'empty',
                      prompt: 'Please select card expiration month'
                    }
                  ]
                },
                card_expire_year: {
                  identifier: 'card_expire_year',
                  rules: [
                    {
                      type: 'regExp',
                      value: /\d{4}/
                    }
                  ]
                },

              },
            });


  $('.ui.modify-info.form')
    .form({
      fields: {
        password1: {
          identifier: 'old_password',
          rules: [
            {
              type   : 'empty',
              prompt : 'Please enter your password'
            }
          ]
        },
        password1: {
          identifier: 'password1',
          optional: true,
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

function progressPayModal() {
  $('.ui.small.modal').modal('show');

  // progressing setting
  var
    $progress       = $('.ui.progress'),
    $button         = $(this),
    updateEvent
  ;
  // restart to zero
  clearInterval(window.fakeProgress);
  $progress.progress('reset');
  // updates every 20ms until complete
  window.fakeProgress = setInterval(function() {
    $progress.progress('increment');
    $button.text( $progress.progress('get value') );
      // stop incrementing when complete
    if($progress.progress('is complete')) {
      clearInterval(window.fakeProgress)
      $(".ui.confirm.modal").modal('show');
    }
  }, 20);

  // progress bar setting
  $('.ui.progress')
    .progress({
      duration : 100,
      total    : 100,
      text     : {
        active: '{value} of {total} done'
      }
    });

  $('.ui.form').form({
    fields: {
      color: {
        identifier: 'card[number]',
        rules: [{
          type: 'regExp',
          value: /\d{4}-\d{4}-\d{4}-\d{4}/i,
        }]
      }
    }
  });
}