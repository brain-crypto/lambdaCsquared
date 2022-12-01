lightTheme = true;
twoColor = true;
blank = true;
expand = false; 
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
$(function () { 
    $(".login-popover").popover();    
 });
 
function changeColor() {
    if (lightTheme) {
        var color1 = "#000000";
        if (twoColor) {
            var color2 = "#404080";
        } else {
            var color2 = color1;
        }
    } else {
        var color1 = "#ffffff";
        if (twoColor) {
            var color2 = "#ccccdd";
        } else {
            var color2 = color1;
        }
    }
    elements = document.getElementsByClassName("random");
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.color = color2;
    }
    elements = document.getElementsByClassName("origin");
    for (let i = 0; i < elements.length; i++) {
        elements[i].style.color = color1;
    }
}

function changeBackground() {
    if (!blank) {
        light = Math.floor(Math.random() * 2);
        ran = Math.floor(Math.random() * 10);
        if (light == 0) {
            document.getElementById("pic").src = "./background/" + ran.toString() + ".jpg";
            lightTheme = false;
        }
        else {
            document.getElementById("pic").src = "./background/10" + ran.toString() + ".jpg";
            lightTheme = true;
        }
        document.getElementById("change").style.display = "inline";
        // elements = document.getElementsByClassName("origin");
        // for (let i = 0; i < elements.length; i++) {
        //     elements[i].style.color = "grey";
        // }    
    } else {
        lightTheme = true;
        document.getElementById("pic").src = "./background/blank.jpg";
        document.getElementById("change").style.display = "none";
    }
    changeColor();
}

$("#color").on("change", function () {
    twoColor = !twoColor;
    changeColor();
});
$("#background").on("change", function () {
    blank = !blank;
    changeBackground();
});

function addText(e) {
    original = document.getElementById('input1').value;
    code = "";
    for (let i = 0; i < original.length; i++) {
        code += '<span class="origin">' + original[i] + '</span><span class="random">' + String.fromCharCode(Math.floor(Math.random() * 5000) + 20000) + '</span>';
    }
    image = document.getElementById('maintext');
    image.innerHTML = code;
    changeColor();
    return false;
}

