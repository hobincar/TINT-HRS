$(function() {
    $('#chat-btn').on('click', () => $('.ui.chat.modal').modal('show'));

    $('#message').on('keyup', function(event) {
        if (event.keyCode == 13) {
            let customer_message = $('#message').val();
            $('#message').val('');
            $('div.comments').append(
                `
                    <div class="comment">
                        <a class="avatar">
                            <img style="height: auto" class="ui round image" src="/static/image/customer.png"/>
                        </a>
                        <div class="content">
                            <a class="author">You</a>
                            <div class="metadata">
                                <span class="date">${new Date().toLocaleTimeString()}</span>
                            </div>
                            <div class="text">
                                ${customer_message}
                            </div>
                        </div>
                    </div>
                `
            );

            $.ajax({
                url: '/chats',
                data: {
                    'message': customer_message
                },
                dataType: 'json',
                success: function (data) {
                    let receptionist_message = data.message;

                    $('div.comments').append(
                        `
                            <div class="comment">
                                <a class="avatar">
                                    <img style="height: auto" class="ui round image" src="/static/image/receptionist.png"/>
                                </a>
                                <div class="content">
                                    <a class="author">Receptionist</a>
                                    <div class="metadata">
                                        <span class="date">${new Date().toLocaleTimeString()}</span>
                                    </div>
                                    <div class="text">
                                        ${receptionist_message}
                                    </div>
                                </div>
                            </div>
                        `
                    );
                }
            });
        }
    });
});