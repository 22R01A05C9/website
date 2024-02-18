function mainfun(){
    const sub_btn = document.getElementById("sub-btn"),
    output_container = document.getElementsByClassName("output-container")[0],
    img = document.getElementsByTagName("img")[0],
    a= document.getElementsByTagName("a")[0],
    form = document.querySelector("form");

    sub_btn.addEventListener("click",()=>{
        xhr = new XMLHttpRequest();
        xhr.open("POST","/qrcode/generate");
        formdata = new FormData(form);
        xhr.send(formdata);
        xhr.onload = ()=>{
            let code = xhr.response;
            if(code){
                img.setAttribute("src",`/static/qr_codes/${code}.png`);
                a.setAttribute("href",`/static/qr_codes/${code}.png`);
                a.setAttribute("download",`${code}.png`);
                output_container.classList.remove("dis-none");
            }
        }
    });
}


setTimeout(mainfun, 1);