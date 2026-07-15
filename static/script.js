// =============================
// AFG AI Script.js (Part 1)
// =============================

// Elements
const sidebar = document.getElementById("sidebar");
const menuBtn = document.getElementById("menuBtn");
const darkMode = document.getElementById("darkMode");

const sendBtn = document.getElementById("sendBtn");
const message = document.getElementById("message");
const chatBox = document.getElementById("chatBox");

const imageBtn = document.getElementById("imageBtn");
const imageInput = document.getElementById("imageInput");

const voiceBtn = document.getElementById("voiceBtn");

const historyBox = document.getElementById("historyBox");

const translateBtn = document.getElementById("translateBtn");
const translateText = document.getElementById("translateText");
const translateResult = document.getElementById("translateResult");


// Sidebar
if(menuBtn){
    menuBtn.onclick = () => {
        sidebar.classList.toggle("show");
    };
}


// Dark Mode
if(darkMode){
    darkMode.onclick = () => {
        document.body.classList.toggle("dark");
    };
}


// Send Message
if(sendBtn){

sendBtn.onclick = async () => {

    const text = message.value.trim();

    if(text === "") return;

    chatBox.innerHTML += `
    <div class="user-message">
        ${text}
    </div>
    `;

    message.value = "";

    const response = await fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:text
        })
    });

    const result = await response.json();

    chatBox.innerHTML += `
    <div class="ai-message">
        ${result.reply}
    </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

};

}


// Enter Key
if(message){

message.addEventListener("keypress",(e)=>{

    if(e.key==="Enter"){

        sendBtn.click();

    }

});

}// =============================
// AFG AI Script.js (Part 2)
// =============================

// Image Upload

if(imageBtn && imageInput){

    imageBtn.onclick = () => {
        imageInput.click();
    };

    imageInput.onchange = async () => {

        const file = imageInput.files[0];

        if(!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try{

            const response = await fetch("/upload",{
                method:"POST",
                body:formData
            });

            const result = await response.json();

            chatBox.innerHTML += `
            <div class="user-message">
                🖼️ عکس پورته شو: ${result.file}
            </div>
            `;

            chatBox.scrollTop = chatBox.scrollHeight;

        }catch(err){

            alert("عکس پورته نه شو.");

        }

    };

}


// Voice Message

if(voiceBtn){

    voiceBtn.onclick = () => {

        if(!("webkitSpeechRecognition" in window)){
            alert("ستاسو براوزر د Voice ملاتړ نه کوي.");
            return;
        }

        const recognition = new webkitSpeechRecognition();

        recognition.lang = "ps-AF";
        recognition.start();

        recognition.onresult = function(event){

            message.value = event.results[0][0].transcript;

        };

    };

}


// Translate

if(translateBtn){

    translateBtn.onclick = () => {

        const text = translateText.value.trim();

        if(text === "") return;

        translateResult.innerHTML = "ژباړه: " + text;

    };

}// =============================
// AFG AI Script.js (Part 3)
// =============================

// Load Chat History

async function loadHistory(){

    if(!historyBox) return;

    try{

        const response = await fetch("/history");
        const data = await response.json();

        historyBox.innerHTML = "";

        if(data.length === 0){

            historyBox.innerHTML = `
            <p>هیڅ پخوانی پیغام نشته.</p>
            `;

            return;
        }

        data.forEach(chat=>{

            historyBox.innerHTML += `
            <div class="user-message">
                👤 ${chat.user}
            </div>

            <div class="ai-message">
                🤖 ${chat.ai}
            </div>
            `;

        });

    }catch(error){

        historyBox.innerHTML = `
        <p>History لوستل نشول.</p>
        `;

    }

}

// Run on page load
loadHistory();

console.log("✅ AFG AI Script Loaded");

