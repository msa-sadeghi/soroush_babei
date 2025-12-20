const colorBoxes = document.querySelectorAll('.color-box')

let myArray = [...colorBoxes]
myArray.forEach(function(cb){
    cb.addEventListener('click', function(event){
        console.log(event.target.style.backgroundColor)
    })
})

document.addEventListener('scroll', function(event){
    console.log(document.documentElement.scrollTop)
})
