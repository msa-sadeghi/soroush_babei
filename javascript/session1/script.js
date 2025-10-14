let citiesData = [
  {city: 'Tehran', temp: 12, weather: 'Sunny', humidity: 23, windSpeed: 32},
  {city: 'Shiraz', temp: 9, weather: 'windy', humidity: 12, windSpeed: 14},
  {city: 'Tabriz', temp: 1, weather: 'rainy', humidity: 43, windSpeed: 12},
  {city: 'Mashhad', temp: 16, weather: 'snowy', humidity: 7, windSpeed: 24},
  {city: 'Esfahan', temp: 23, weather: 'Sunny', humidity: 15, windSpeed: 18},
]


let weather = document.querySelector('.weather')
let button = document.querySelector('button')
let input = document.querySelector('input')


button.addEventListener('click', function(){

    let city = input.value
    let citySelected = citiesData.find(function(c){
        return c.city === city
    })

    if(citySelected){

        weather.classList.remove('loading')
    }
})


function f1(){
    console.log("f1")
}
function f2(){
    console.log("f2")
}
function f3(){
    console.log("f3")
}