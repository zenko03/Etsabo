// Containers
var _conversationContainer = document.querySelector(".conversation-container");
var _messagesContainer = document.querySelector(".messages-container");

var _senderTemplate = document.querySelector("[data-senderContainer]");
var _receiverTemplate = document.querySelector("[data-receiverContainer]");

var _sendMessageButton = document.querySelector(".button-send-message");

var lastMessagesPk = []

function getConverstation(callback) {
    var data = [];

    $.ajax({
        url: "./conversation/?patient=1&medecin=1&est_patient=1",
        dataType: "json",
        type: 'GET',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrfToken);
        },
        success: (response) => {
            callback(response);
        },
        error: function(response) {
            alert("Error occured")
        }
    });

    return data;
}

//#region Message Adder
function addSender(data) {
    let sender = _senderTemplate.content.cloneNode(true);

    addMessage(data, sender);
}
function addReceiver (data) {
    let receiver = _receiverTemplate.content.cloneNode(true);

    addMessage(data, receiver);
}

function addMessage(data, node) {
    let messageContent = node.querySelector(".message");
    messageContent.textContent = data.fields.contenus;

    lastMessagesPk.push(data.pk);

    _messagesContainer.appendChild(node);
}
//#endregion

function populateConversation() {
    getConverstation((response) => {
        let conversations = response

        for (let i = 0; i < conversations.length; i++) {
            let messageData = conversations[i];
            if (lastMessagesPk.includes(messageData.pk)) continue;

            let estPatient = parseInt(_conversationContainer.dataset.estpatient);
    
            let messageSenderType = parseInt(messageData.fields.type);
            console.log(messageData)
            if (estPatient == messageSenderType) addSender(messageData);
            else addReceiver(messageData); 
        }
    });
     
}

$(document).ready(function () {
        setInterval(() => {
            populateConversation();
        }, 1000)
    
});

function sendMessageTo(message) {
    $.ajax({
        url: `./send?patient=1&medecin=1&est_patient=0&message=${ message }`,
        dataType: "json",
        type: 'GET',
        success: (response) => {
            
        },
        error: function(response) {

        }
    });
}

$(".button-send-message").click(function (e) { 
    e.preventDefault();
    
    var textMessage = $("#message-send").val();
    sendMessageTo(textMessage);

    $("#message-send").val("");
});