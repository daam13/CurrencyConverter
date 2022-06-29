const backend = 'http://localhost:5000';
let initialC, finalC, amount;
let currencies = ['CRC', 'JPY', 'EUR', 'USD', 'GBP', 'MXN', 'VEF'];

function formIsValid(initialC, finalC, value) {
    if (initialC != '' && finalC != '' && value != '') {
        return true;
    }
    return false;
}

// method get  

function getResult() {
    const request = new Request(`${backend}/convert?from=${initialC}&to=${finalC}&amount=${amount}`, {method: 'GET', headers: {} });
    (async () => {
        try {
            const response = await fetch(request);
            if (!response.ok) {
                throw new Error();
            } else {
                let div = document.querySelector('#result')
                div.innerHTML = `<h1>Result ${parseFloat((await response.json()).result).toFixed(2)}</h1>`;
                div.classList.toggle('badge');
                div.classList.toggle('bg-success');
            }
        } catch (e) {
            alert('response failed');
        }
    })();
}


function loaded(){
    
    
    
    // event listener
    document.querySelector('#convertBtn').addEventListener('click', (e) => {
        e.preventDefault();
        
        initialC = document.getElementById('initialCurrency').value;
        finalC = document.getElementById('finalCurrency').value;
        amount = document.getElementById('amount').value;

        if(formIsValid(initialC, finalC, amount)) {
            getResult();
        } else alert('error');
    })


}

document.addEventListener("DOMContentLoaded",loaded);