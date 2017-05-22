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
        }

        if (step == 2) {
            $('#reservation-summary').show();
            $('#check-in').text($('input[name=check_in]').val());
            $('#check-out').text($('input[name=check_out]').val());
            $('#n-room').text($('input[name=n_room]').val());
            $('#n-adult').text($('input[name=n_adult]').val());
            $('#n-child').text($('input[name=n_child]').val());
            $('#coupon').text($('input[name=coupon]').val() || "No coupon");
        }

        if (step == 3) {
        }

        if (step == 4)
            $('#next-btn').hide();
        $('#prev-btn').show();

        $('html, body').animate({
            scrollTop: $("#header").offset().top
        }, 500);
    });

    $('#prev-btn').on('click', () => {
        if (step > 1) {
            $(`#step${step}-nav`).switchClass('active', 'disable');
            $(`#step${step}`).hide();
            step--;
            $(`#step${step}`).show();
            $(`#step${step}-nav`).switchClass('completed', 'active');

            if (step == 1) {
                $('#reservation-summary').hide();
                $('#prev-btn').hide();
            }
            $('#next-btn').show();

            $('html, body').animate({
                scrollTop: $("#header").offset().top
            }, 500);
        }
    });


  $('.ui.dropdown').dropdown();
})