function resrce1(){
    fetch('https://muminae100.github.io/flask/books/all')
    .then(response => response.json()
    ) 
    .then(json =>{
       console.log(json)
            
            
    })   
  
}
resrce1();
