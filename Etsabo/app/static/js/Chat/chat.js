// Containers
var conversationContainer = document.querySelector(".conversation-container");

var senderTemplate = document.querySelector("[data-senderContainer]");
var receiverTemplate = document.querySelector("[data-receiverContainer]");

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
    let sender = senderTemplate.content.cloneNode(true);

    addMessage(data, sender);
}
function addReceiver (data) {
    let receiver = receiverTemplate.content.cloneNode(true);

    addMessage(data, receiver);
}

function addMessage(data, node) {
    let messageContent = node.querySelector(".message");
    messageContent.textContent = data.fields.contenus;

    lastMessagesPk.push(data.pk);

    conversationContainer.appendChild(node);
}
//#endregion

function populateConversation() {
    getConverstation((response) => {
        let conversations = response

        for (let i = 0; i < conversations.length; i++) {
            let messageData = conversations[i];
            if (lastMessagesPk.includes(messageData.pk)) continue;

            let estPatient = parseInt(conversationContainer.dataset.estpatient);
    
            let messageSenderType = parseInt(messageData.fields.type);
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