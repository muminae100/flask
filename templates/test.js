function resrce1(){
    fetch('http://127.0.0.1:5000/books/all')
    .then(response => response.json()
    ) 
    .then(json =>{
       console.log(json)
            
            
    })   
  
}
resrce1();
