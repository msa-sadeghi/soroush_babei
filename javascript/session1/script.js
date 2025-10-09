let username = document.querySelector('.username')
let password = document.querySelector('.password')
let modal = document.querySelector('.modal')
let button = document.querySelector('button')


button.addEventListener('click', 
    function dataValidation(){
    let usernameVal = username.value
    let passwordVal = password.value

    if(usernameVal.length < 12 || passwordVal.length < 8){
        modal.style.background = 'red'
        modal.innerHTML = "اطلاعات نادرست است"
        modal.style.display = 'inline'
    }else{
        modal.style.background = 'green'
        modal.innerHTML = "اطلاعات درست است"
        modal.style.display = 'inline'

        password.classList.add("red")

    }

    setTimeout(function(){
        modal.style.display = "none"
    }, 3000)
}
)


function myFocus(){
    console.log("focus")
    username.style.border = "2px solid red"
}

function myBlur(){
    console.log("blur")
    username.style.border = ""
}

function MydblClick(){
    console.log("blalal")
}


let s = document.getElementById("countries")
function changeHandler(){
    console.log(s.value)
}