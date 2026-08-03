function backHome(){
    location.reload();
}


function openFeature(title){
    document.body.innerHTML = `
    <div style="padding:20px;text-align:center;font-family:Arial;">
        <h2>${title}</h2>

        <button onclick="backHome()"
        style="
        padding:12px 30px;
        border-radius:10px;
        border:none;
        font-size:16px;">
        ⬅️ Back
        </button>
    </div>
    `;
}


// 🧠 AI Memory
function showMemory(){

let memory = localStorage.getItem("afg_memory") || "";

let text = prompt(
"🧠 خپله یادونه ولیکه:",
memory
);

if(text){

localStorage.setItem(
"afg_memory",
text
);

alert("✅ Memory Save شوه");

}

}


// ⭐ Favorites
function showFavorites(){

let fav = localStorage.getItem("afg_favorites") || "";

let text = prompt(
"⭐ خپل Favorite ولیکه:",
fav
);

if(text){

localStorage.setItem(
"afg_favorites",
text
);

alert("✅ Favorite Save شو");

}

}


// 📌 Saved Answers
function showSaved(){

let saved = localStorage.getItem("afg_saved_answers") || "";

let text = prompt(
"📌 خپل Saved Answer ولیکه:",
saved
);

if(text){

localStorage.setItem(
"afg_saved_answers",
text
);

alert("✅ Saved Answer خوندي شو");

}

}


// 📂 My Files
function showFiles(){

let files = localStorage.getItem("afg_files") || "";

let text = prompt(
"📂 د فایل نوم یا معلومات ولیکه:",
files
);

if(text){

localStorage.setItem(
"afg_files",
text
);

alert("✅ File معلومات Save شول");

}

}


// 🎨 Theme
function showTheme(){

if(document.body.style.background === "black"){

document.body.style.background="white";
document.body.style.color="black";

}else{

document.body.style.background="black";
document.body.style.color="white";

}

}


// 🔔 Notifications
function showNotifications(){

let note = localStorage.getItem("afg_notifications") || "";

let text = prompt(
"🔔 خپله خبرتیا ولیکه:",
note
);

if(text){

localStorage.setItem(
"afg_notifications",
text
);

alert("✅ Notification Save شو");

}

}


// 🌍 Languages
function showLanguages(){

let lang = localStorage.getItem("afg_language") || "Pashto";

let text = prompt(
"🌍 ژبه وټاکه (Pashto / English / Dari):",
lang
);

if(text){

localStorage.setItem(
"afg_language",
text
);

alert("✅ Language Save شوه");

}

}


// 📷 Image AI
function showImageAI(){

alert("📷 Image AI به ژر فعال شي");

}


// 💎 Premium
function showPremium(){

alert("💎 Premium / Payments\n\nدا برخه د راتلونکي لپاره ده.");

}
