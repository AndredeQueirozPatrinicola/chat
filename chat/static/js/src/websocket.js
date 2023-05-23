const roomName = JSON.parse(document.getElementById('room-name').textContent);
const userId = document.getElementsByClassName('user-id')[0].id

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + "?"
);

chatSocket.onopen = (e) => {
    console.log("Connection openned")
}

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const message = `[${data.user.username}] : ${data.message} \n`
    document.querySelector('#chat-log').value += message;
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};


document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'user' : userId,
        'message': message
    }));
    messageInputDom.value = '';
};