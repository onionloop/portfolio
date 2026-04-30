const texts = [
    ". HEY, WHAT'S UP?",
    ". OPEN TO COLLABS",
    ". GIT PUSH",
    ". GIT PUSH",
    ". PULL",
    ". POP",
    "> sudo chmod +x future"

    
];

let index = 0;
const foot_texts = document.getElementById("dynamic-text");

function changeText(){

    foot_texts.textContent = texts[index];
    index = (index + 1) % texts.length;
}

setInterval(changeText, 2000)

