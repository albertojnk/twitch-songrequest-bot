
document.getElementById("btn-login").addEventListener("click", function (e) {
    backend_url = "http://localhost:5000/twitch/oauth"
    const http = new XMLHttpRequest();
    http.open("GET", backend_url);
    http.send();
    http.onreadystatechange=(e)=>{
        window.location.href = "http://localhost:5000"
    }
    e.preventDefault()    
})


function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * 
 charactersLength));
   }
   return result;
}