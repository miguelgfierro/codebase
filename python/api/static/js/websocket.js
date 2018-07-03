$(document).ready(function () {
    // Use a "/test" namespace.
    // An application can open a connection on multiple namespaces, and
    // Socket.IO will multiplex all those connections on a single
    // physical channel. If you don't care about multiple channels, you
    // can set the namespace to an empty string.
    // namespace = '/test';
    namespace = '';

    // Connect to the Socket.IO server.
    // The connection URL has the following format:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    // socket.on('message', function (data) {
    //     console.log('message form backend ' + data);
    // });

    // socket.on('alert', function (data) {
    //     alert('Alert Message!! ' + data);
    // });

    // function json_button() {
    //     socket.send('json_button', '{"message": "test"}');
    // }

    // function alert_button() {
    //     socket.send('alert_button', 'Message from client!!')
    // }


    // this is a callback that triggers when the "my response" event is emitted by the server.
    // socket.on('my response', function (msg) {
    //     $('#log').append('<p>Received: ' + msg.data + '</p>');
    // });
    // //example of triggering an event on click of a form submit button
    // $('form#emit').submit(function (event) {
    //     socket.emit('my event', { data: $('#emit_data').val() });
    //     return false;
    // });


    // Interval function that tests message latency by sending a "ping"
    // message. The server then responds with a "pong" message and the
    // round trip time is measured.
    var ping_pong_times = [];
    var start_time;
    window.setInterval(function () {
        start_time = (new Date).getTime();
        socket.emit('my_ping');
    }, 1000);

    // Handler for the "pong" message. When the pong is received, the
    // time from the ping is stored, and the average of the last 30
    // samples is average and displayed.
    socket.on('my_pong', function () {
        var latency = (new Date).getTime() - start_time;
        ping_pong_times.push(latency);
        ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
        var sum = 0;
        for (var i = 0; i < ping_pong_times.length; i++)
            sum += ping_pong_times[i];
        $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
    });

});
