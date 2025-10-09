let countrySelect = document.querySelector('.countrySelect')
let citySelect = document.querySelector('.citySelect')

let cdata = {
    Iran: ['tehran', 'zahedan'],
    Turkey: ['ist', 'ez']
}

countrySelect.addEventListener('change', function(){
    let selected = countrySelect.value
    let cities = cdata[selected]
    citySelect.innerHTML = ""

    cities.forEach(function(city){
        citySelect.innerHTML += `<option>${city}</option>`
    });
})