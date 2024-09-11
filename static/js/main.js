import Apps from "./apps.js";
import Carts from "./carts.js";
import Orders from "./orders.js";
import Payments from "./payments.js";
import Customers from "./customers.js";
import Security from "./security.js";

let navStack = new Array();
const mainContent = document.querySelector(".main");
const navModal = document.querySelector("#navModal");
const navModalHeader = navModal.querySelector(".modal-header");
const navModalBody = navModal.querySelector(".modal-body");
const closeButtons = document.querySelectorAll(".close");
const navBar = document.querySelector(".nav-bar");
closeButtons.forEach((button) => {
  button.onclick = () => {
    navModal.style.display = "none";
  };
});
navBar.onclick = (event) => {
  if (navStack.length && event.target.classList.contains("nav-btn")) {
    navStack[navStack.length - 1].classList.remove("active");
    navStack.pop();
    event.target.classList.add("active");
    navStack.push(event.target);
  }

  if (event.target.id === "apps") {
    mainContent.innerHTML = Apps();
  } else if (event.target.id === "carts") {
    mainContent.innerHTML = Carts();
  } else if (event.target.id === "customers") {
    mainContent.innerHTML = Customers();
  } else if (event.target.id === "orders") {
    mainContent.innerHTML = Orders();
  } else if (event.target.id === "payments") {
    mainContent.innerHTML = Payments();
  } else if (event.target.id === "security") {
    mainContent.innerHTML = Security();
  }
};

window.onclick = (event) => {
  if (event.target == navModal) {
    navModal.style.display = "none";
  }
};
const apps = document.querySelector("#apps");
apps.classList.add("active");
navStack.push(apps);
mainContent.innerHTML = Apps();
