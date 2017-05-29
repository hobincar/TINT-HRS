step = 1;

$(document)
.ready(function() {
    $('#next-btn').on('click', () => {
        if (step < 4) {
            $(`#step${step}-nav`).switchClass('active', 'completed');
            $(`#step${step}`).hide();
            step++;
            $(`#step${step}`).show();
            $(`#step${step}-nav`).switchClass('disable', 'active');

            $('html, body').animate({
                scrollTop: $("#header").offset().top
            }, 500);
        }

        if (step == 2) {
            $('#prev-btn').show();

            $('#reservation-summary').show();
            $('#check-in').text($('input[name=check_in]').val());
            $('#check-out').text($('input[name=check_out]').val());
            $('#n-adult').text($('input[name=n_adult]').val());
            $('#n-child').text($('input[name=n_child]').val());
            $('#coupon').text($('input[name=coupon]').val() || "No coupon");
        }
        else if (step == 3) {
            let room_desc = "";
            for (room of $('.room-item')) {
                let n_room = $(room).find('input[name=n_room]').val();
                if (n_room > 0) {
                    let room_type = $(room).find('.room-type').text();
                    room_desc += `${n_room} ${room_type}, `;
                }
            }
            room_desc = room_desc.slice(0,-2);
            $('#room').text(room_desc);

            $('#room-item').show();
        }
        else if (step == 4) {
            $('#next-btn').hide();

            let n_breakfast = $('input[name=n_breakfast]').val();
            let n_baby_bed = $('input[name=n_baby_bed]').val();
            let n_stay = (Date.parse($('input[name=check_out]').val()) - Date.parse($('input[name=check_in]').val())) / 86400000;
            let room_cost = 0;
            for (room of $('.room-item')) {
                let n_room = $(room).find('input[name=n_room]').val();
                let cost_per_night = parseFloat($(room).find('.cost-per-night').text());
                room_cost += n_room * cost_per_night;
            }
            let discount = parseInt($('input[name=coupon]').val());
            let total_cost = room_cost + (16.5 * n_breakfast) + (10 * n_baby_bed);
            if (!isNaN(discount))
                total_cost = total_cost / 100 * (100-discount);

            $('#n-breakfast').text(`${n_breakfast} Breakfast`);
            $('#n-baby-bed').text(`${n_baby_bed} Baby Bed`);
            $('#total-cost').text(`${total_cost}`);
            $('#pay-submit-btn').text(`Pay for $${total_cost}`);

            $('#breakfast-item').show();
            $('#n-baby-bed-item').show();
            $('#total-cost-item').show();
        }
    });

    $('#prev-btn').on('click', () => {
        if (step > 1) {
            $(`#step${step}-nav`).switchClass('active', 'disable');
            $(`#step${step}`).hide();
            step--;
            $(`#step${step}`).show();
            $(`#step${step}-nav`).switchClass('completed', 'active');

            $('html, body').animate({
                scrollTop: $("#header").offset().top
            }, 500);
        }

        if (step == 1) {
            $('#reservation-summary').hide();
            $('#prev-btn').hide();
        }
        else if (step == 2) {
            $('#room-item').hide();
        }
        else if (step == 3) {
            $('#next-btn').show();

            $('#breakfast-item').hide();
            $('#n-baby-bed-item').hide();
            $('#total-cost-item').hide();
        }
    });


    $('.ui.dropdown').dropdown();
    $('.ui.toggle.checkbox').checkbox('set checked');
});

function progressModal() {
  // show modal
  $('.ui.pay.modal')
    .modal('show')
  ;

  // progressing setting
  var
    $progress       = $('.ui.progress'),
    $button         = $(this),
    updateEvent
  ;
    // restart to zero
  clearInterval(window.fakeProgress)
  $progress.progress('reset');
    // updates every 20ms until complete
  window.fakeProgress = setInterval(function() {
    $progress.progress('increment');
    $button.text( $progress.progress('get value') );
      // stop incrementing when complete
    if($progress.progress('is complete')) {
      clearInterval(window.fakeProgress)
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
    })
  ;
}