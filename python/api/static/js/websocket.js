$(document).ready(function () {
    // Use a "/test" namespace.
    // An application can open a connection on multiple namespaces, and
    // Socket.IO will multiplex all those connections on a single
    // physical channel. If you don't care about multiple channels, you
    // can set the namespace to an empty string.
    // namespace = "/test";
    var namespace = "";

    // Connect to the Socket.IO server.
    // The connection URL has the following format:
    //     http[s]://<domain>:<port>[/<namespace>]
    var socket = io.connect(location.protocol + "//" + document.domain + ":" + location.port + namespace);



    // JS to send a message to the server. Their html counterpart is
    // <form id="emit" method="POST" action="#">.
    // This sends to the server the text content of id="emit_data".
    // In python, the message is handled via the tag "my_event".
    $("form#emit").submit(function (event) {
        socket.emit("my_event", { data: $("#emit_data").val() });
        return false;
    });

    // JS to receive the a response message from the server. In python, the
    // message is emitted with the tag "my_response". Their html counterpart
    // is <div id="response"></div>.
    socket.on("my_response", function (msg) {
        $("#response").append("<br>" + $("<div/>")
            .text("Response from server: " + msg.data + " (note: " + msg.note + ")")
            .html());
    });

    // Interval function that tests message latency by sending a "ping"
    // message. The server then responds with a "pong" message and the
    // round trip time is measured.
    var pingPongTimes = [];
    var startTime;
    window.setInterval(function () {
        startTime = (new Date).getTime();
        socket.emit("my_ping");
    }, 1000);

    // Handler for the "pong" message. When the pong is received, the
    // time from the ping is stored, and the average of the last 30
    // samples is average and displayed.
    socket.on("my_pong", function () {
        var latency = (new Date).getTime() - startTime;
        pingPongTimes.push(latency);
        pingPongTimes = pingPongTimes.slice(-30); // keep last 30 samples
        var sum = 0;
        for (var i = 0; i < pingPongTimes.length; i++) {
            sum += pingPongTimes[i];
        }
        $("#ping-pong").text(Math.round(10 * sum / pingPongTimes.length) / 10);
    });



});
