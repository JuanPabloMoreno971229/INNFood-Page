let ubicacioPrincipal = window.pageYOffset;

window.addEventListener("scroll", function() {
    let desplazamientoActual = window.pageYOffset;
    if (ubicacioPrincipal >= desplazamientoActual) {
        document.getElementsByTagName("nav")[0].style.top = "0px"
    } else {
        document.getElementsByTagName("nav")[0].style.top = "-100px"
    }
    ubicacioPrincipal = desplazamientoActual;
})

//Menú

let enlacesHeader = document.querySelectorAll(".enlaces-header")[0];
let semaforo = true;

document.querySelectorAll(".hamburger")[0].addEventListener("click", function() {
    if (semaforo) {
        document.querySelectorAll(".hamburger")[0].style.color = "#F2CA4C";
        semaforo = false;
    } else {
        document.querySelectorAll(".hamburger")[0].style.color = "#008080";
        semaforo = true;
    }

    enlacesHeader.classList.toggle("menudos")
})