const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");

fileInput.addEventListener("change", function(){

const file = this.files[0];

if(file){

const reader = new FileReader();

reader.addEventListener("load", function(){
preview.setAttribute("src", this.result);
preview.style.display = "block";
});

reader.readAsDataURL(file);

}

});