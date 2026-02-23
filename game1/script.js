let advice = document.getElementById("advice");
let tap = document.getElementById("cir");
let text1 = document.getElementById("te");
let text2 = document.getElementById("te1");
let circle = document.getElementById("cir");
let but1 = document.getElementById("but1");
let onoff1 = document.getElementById("onoff");

let colora = localStorage.getItem("colora") ? localStorage.getItem("colora") : 16777215;
let leftcolora = parseInt(16777215 - colora);
let isauto = false;
let autospeed1 = 16777216;
let autospeed2 = 10;
let level = localStorage.getItem("level") ? parseInt(localStorage.getItem("level")) : 0;
let isbut1on = true;

text1.innerText = "#" + parseInt(colora).toString(16).toUpperCase();
text2.innerText = colora;
circle.style.backgroundColor = "#" + parseInt(colora).toString(16).toUpperCase();
but1.innerHTML = `auto <br> lv.${level} ${level}/s <br> a`
autospeed1 = 1000 / level;
localStorage.setItem("level", level);
if (level >= 1) {
  auto1();
}

tap.addEventListener("click", () => {
  tapi();
});

tap.addEventListener("touch", () => {
  tapi();
});

document.addEventListener("contextmenu", function (event) {
  //event.preventDefault();
});

let first10 = function f10() {
  if (leftcolora <= 256) {
    advice.innerHTML = "(" + (256 - leftcolora) + ")";
  } else {
    advice.innerHTML = "";
    first10 = function f10() {};
  }
};

first10();

function tapi() {
  if (colora > 0) {
    colora--;
    leftcolora = 16777215 - colora;
    circle.style.backgroundColor = "#" + colora.toString(16).toUpperCase();
    text1.innerText = "#" + colora.toString(16).toUpperCase();
    text2.innerText = colora;
    localStorage.setItem("colora", colora);
    first10();
  }
}

function tapi5() {
  if (colora > 0) {
    colora -= 5;
    leftcolora = 16777215 - colora;
    circle.style.backgroundColor = "#" + colora.toString(16).toUpperCase();
    text1.innerText = "#" + colora.toString(16).toUpperCase();
    text2.innerText = colora;
    localStorage.setItem("colora", colora);
    first10();
  }
}

function auto1() {
  if (isbut1on) {
    setTimeout(() => {
      tapi();
      auto1();
    }, autospeed1);
  }
}

function but() {
    level += 1;
  but1.innerHTML = `auto <br> lv.${level} ${level}/s<br> a`
  autospeed1 = 1000 / level;
  localStorage.setItem("level", level);
  if (level == 1) {
    auto1();
  }
}

function onoff() {
  if (isbut1on) {isbut1on = false; onoff1.innerHTML = "false";}
  else {isbut1on = true; onoff1.innerHTML = "true"; auto1();}
}

function push() {
  if (!isauto) {
    isauto = true;
    tt();
  } else {
    isauto = false;
  }
}

function tt() {
  setTimeout(() => {
    tapi();
    if (isauto) {
      tt();
    }
  }, autospeed2);
}

function ris() {
  colora = 16777215;
  localStorage.setItem("colora", 16777215);
  localStorage.setItem("level", 0);
  circle.style.backgroundColor = "#FFFFFF";
  text1.innerText = "#FFFFFF";
  text2.innerText = 16777215;
  but1.innerHTML = `auto <br> lv.0 0/s<br> a`
  isauto = false;
  level = 0;
  first10();
  window.location.reload(true);
}
