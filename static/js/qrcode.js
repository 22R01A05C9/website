function mainfun(){
    const sub_btn = document.getElementById("sub-btn"),
    output_container = document.getElementsByClassName("output-container")[0],
    img = document.getElementsByTagName("img")[0],
    a= document.getElementsByTagName("a")[0],
    form = document.querySelector("form"),
    imp = document.getElementsByTagName("input")[0],
    space = document.getElementsByClassName("space")[0],
    arrow = document.getElementsByClassName("arrow")[0],
    info = document.getElementsByClassName("info")[0];

    sub_btn.addEventListener("click",()=>{
        if(imp.value == ""){
            imp.style.border = "3px solid Red";
            imp.style.boxShadow = "0 0 0 0";
            space.classList.remove("dis-none");
            info.classList.remove("dis-none");
            arrow.classList.remove("dis-none");
            imp.addEventListener("focus", ()=>{
                space.classList.add("dis-none");
                info.classList.add("dis-none");
                arrow.classList.add("dis-none");
                imp.style.border = "1px solid blue";
                imp.style.boxShadow = "2px 1px 1px 1px";
            });
            return;
        }
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