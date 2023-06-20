function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}





let btns= document.querySelectorAll(".product_cart button")

btns.forEach(btn=>
    {
        btn.addEventListener("click",addToCart)
    })

    function addToCart(e){
        let data_num = e.target.value        
        let url = "/mycart"
        
        let data = {num:data_num}
        
        fetch(url,{
            method:"POST",
            headers:{"Content-Type":"application/json",'X-CSRFToken': csrftoken},
            body: JSON.stringify(data)
        })
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
        })
        .catch(error=>{
            console.log(error)
        })

    }
