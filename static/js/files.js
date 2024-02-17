function mainone(){
    const fileclass = document.querySelector(".uploader"),
    inp = document.getElementById("file-input"),
    inputs = document.querySelectorAll(".code-input input"),
    button = document.getElementById("down-sub-btn"),
    download_class = document.getElementsByClassName("download")[0],
    info = document.getElementsByClassName("info")[0],
    filename = document.getElementById("file-name"),
    percent = document.getElementById("percent"),
    progress = document.getElementsByClassName("progress")[0],
    status = document.getElementById("status"),
    upload_status = document.getElementsByClassName("upload-status")[0],
    form = document.getElementById("form"),
    upload_result = document.getElementsByClassName("upload-result")[0],
    form2 = document.getElementById("form2"),
    dinfo = document.getElementsByClassName("dinfo")[0],
    fname=document.getElementsByClassName("fname")[0],
    down = document.getElementsByClassName("down")[0],
    a=document.getElementById("a"),
    code = document.getElementById("code");

    
    inputs[0].focus();

    inputs.forEach((input,index1) => {
        input.addEventListener("keyup", (e) => {
            const currentinput = input,
            nextinput = input.nextElementSibling,
            previnput = input.previousElementSibling;

            if(nextinput && nextinput.hasAttribute("disabled") && currentinput.value!==""){
                nextinput.removeAttribute("disabled");
                nextinput.focus();
            }

            if(nextinput == null && currentinput.value.length >= 1 && e.key==="Enter"){
                button.click();
            }

            if(currentinput.value.length > 1){
                currentinput.value = currentinput.value.substring(0,1);
                nextinput.removeAttribute("disables");
                nextinput.focus();
                return;
            }


            if(e.key === "Backspace"){
                inputs.forEach((input,index2) => {
                    if(index1 <= index2 && previnput) {
                        input.setAttribute("disabled",true);
                        currentinput.value = "";
                        previnput.focus();
                    }
                });
            }

            if(!inputs[3].disabled && inputs[3].value !== ""){
                button.classList.add("active");
                return;
            }
            button.classList.remove("active");
        });
    });

    fileclass.addEventListener("click", () => {
        inp.click();
    })

    inp.onchange = ({target}) => {
        download_class.classList.add("dis-none")
        file = target.files[0];
        if( file.size > 4000000000){
            info.classList.remove("dis-none");
            return;
        }
        else{
            info.classList.add("dis-none");
            status.classList.remove("dis-none");
            upload_status.classList.remove("dis-none");
            const fname = file.name;
            if(fname.length > 20){
                let lst = fname.split(".");
                let ext = lst[lst.length-1];
                let strnme = lst[0].substring(0,6);
                let endnme = lst[0].substring(lst[0].length-6,lst[0].length -1);
                const fnme = strnme + "...." + endnme + "." + ext;
                filename.innerHTML = fnme;
            }
            else{
                filename.innerHTML = fname;
            }
            let xhr = new XMLHttpRequest();
            xhr.open("POST","/files");
            xhr.upload.addEventListener("progress", ({loaded,total}) => {
                let p = Math.round((loaded/total)*100);
                percent.innerHTML = p+"%"; //p.tofixed(1)
                progress.style.width = p+"%"; 
            });
            let formdata = new FormData(form);
            xhr.send(formdata);
            xhr.onload = () => {
                let code1 = xhr.response;
                code.innerHTML = code1;
                upload_result.classList.remove("dis-none");
            }
        }    
    }

    button.addEventListener("click", () => {
        xhr1 = new XMLHttpRequest();
        xhr1.open("POST","/files/download");
        let formdata1 = new FormData(form2);
        xhr1.send(formdata1);
        xhr1.onload = () =>{
            let res = xhr1.response;
            if (res==="Error:404--NOT-Found"){
                dinfo.classList.remove("dis-none");
                down.classList.add("dis-none");
            }
            else{
                dinfo.classList.add("dis-none");
                let data = JSON.parse(res)
                down.classList.remove("dis-none");
                fname.innerHTML=data.name;
                a.setAttribute("href",`/static/files/${data.code}/${data.name}`);
                a.setAttribute("download",data.name);
            }
        }
    });

}

setTimeout(mainone,1);