const sendBtn = document.getElementById("sendBtn");
const message = document.getElementById("message");
const chatBox = document.getElementById("chatBox");

sendBtn.onclick = function(){

    let text = message.value.trim();

    if(text === ""){
        return;
    }

    let user = document.createElement("div");
    user.className = "user-message";
    user.innerHTML = text;

    chatBox.appendChild(user);

    message.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;


    setTimeout(function(){

        let ai = document.createElement("div");
        ai.className = "ai-message";

        ai.innerHTML =
        "🤖 AFG AI: ستا پیغام ترلاسه شو، لږ انتظار...";

        chatBox.appendChild(ai);

        chatBox.scrollTop = chatBox.scrollHeight;

    },800);

};
// Menu control
const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
const closeMenu = document.getElementById("closeMenu");

menuBtn.onclick = function(){
    sidebar.classList.add("show");
};

closeMenu.onclick = function(){
    sidebar.classList.remove("show");
};


// Dark mode
const darkBtn = document.getElementById("darkBtn");

darkBtn.onclick = function(){

    document.body.classList.toggle("dark");

};


// Image button
const imageBtn = document.getElementById("imageBtn");
const imageInput = document.getElementById("imageInput");

imageBtn.onclick = function(){
    imageInput.click();
};


// Voice button
const voiceBtn = document.getElementById("voiceBtn");

voiceBtn.onclick = function(){

    if("webkitSpeechRecognition" in window){

        let speech = new webkitSpeechRecognition();

        speech.lang = "ps-AF";

        speech.start();

        speech.onresult = function(event){

            message.value =
            event.results[0][0].transcript;

        };

    }else{

        alert("Voice support نشته");

    }

};
// AI Server Connection

async function askAI(text){

    try{

        let response = await fetch(
            "http://YOUR_SERVER_IP:5000/chat",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    message:text
                })
            }
        );


        let data = await response.json();


        let ai = document.createElement("div");
        ai.className="ai-message";

        ai.innerHTML =
        "🤖 AFG AI: " + data.reply;


        chatBox.appendChild(ai);


    }catch(error){

        let ai = document.createElement("div");
        ai.className="ai-message";

        ai.innerHTML =
        "⚠️ سرور سره اړیکه نشته";


        chatBox.appendChild(ai);

    }

}
