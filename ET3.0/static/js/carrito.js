$(document).ready(function abrirmodal(){
    //Para abrir y cerrar un modal(popup )
    btnopenmodal = document.querySelector("#open")
    const btncerrarmodal = document.querySelector("#close")
    const modal = document.querySelector("#modal");btnopenmodal.addEventListener("click",()=>{
    modal.showModal();
     });
    btncerrarmodal.addEventListener("click",()=>{
      modal.close();
    });
//fin de evento popup

});