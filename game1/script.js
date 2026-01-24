let advice = document.getElementById("advice");
let tap = document.getElementById("cir");
let text1 = document.getElementById("te");
let text2 = document.getElementById("te1");
let circle = document.getElementById("cir");

let colora = localStorage.getItem("colora")
  ? localStorage.getItem("colora")
  : 16777215;
let leftcolora = parseInt(16777215 - colora);
let isauto = false;
let vact = false;
let autospeed1 = 16777216;
let autospeed2 = 10;

text1.innerText = "#" + parseInt(colora).toString(16).toUpperCase();
text2.innerText = colora;
circle.style.backgroundColor =
  "#" + parseInt(colora).toString(16).toUpperCase();

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
    console.log(leftcolora, 256 - leftcolora);
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
  } else {
    alert("おめ暇人");
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
  } else {
    alert("おめ暇人");
  }
}

function auto1() {
  if (vact) {
    setTimeout(() => {
      tapi();
      auto1();
      console.log("auto");
    }, autospeed1);
  }
}

auto1();

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
  circle.style.backgroundColor = "#FFFFFF";
  text1.innerText = "#FFFFFF";
  text2.innerText = 16777215;
  isauto = false;
}
