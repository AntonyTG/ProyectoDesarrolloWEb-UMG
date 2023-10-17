let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        
        listElement.classList.toggle('arrow');

        let heitht = 0;
        let menu = listElement.nextElementSibling;
        if(menu.clientHeight == "0"){
            heitht = menu.scrollHeight;
        }
        
        menu.style.heitht = '${heitht}px'; 
    })
});