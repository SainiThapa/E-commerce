//Find out the cart items from Local Storage 
if (localStorage.getItem('cart')==null){
    var cart={};
  }
  else{
      cart=JSON.parse(localStorage.getItem('cart'));
 
      document.getElementById('cart').innerHTML = Object.keys(cart).length;
  }

//if the AddtoCart is clicked, add/increment the item

  $('.product_cart').click(function(){
    var idstr= this.id.toString();
    console.log(idstr);
    if(cart[idstr]!=undefined){
      cart[idstr]+=1;
    }
    else{
      cart[idstr]=1;
    }
    updateCart(cart);
    console.log(cart);
    localStorage.setItem('cart',JSON.stringify(cart)); 
  });

function updateCart(cart){
  for(var item in cart){
      document.getElementById('div'+item).innerHTML="<button id='minus"> + item + "'class= 'btn btn-primary minus'>-</button> <span id='val"+item+"''>"+cart[item]+"</span> <button id='plus"+item+"'class=btn btn-primary plus'>+</button>"
  }
}

//