const backend = 'http://localhost:8000';

let currencies = ['CRC', 'JPY', 'EUR', 'USD', 'GBP', 'MXN', 'VEF'];

function fillCurrenciesCB(){

}

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
                document.querySelector('#result').innerHTML = (await response.json()).result;
            }
        } catch (e) {
            alert('response failed');
        }
    })();
}


function loaded(){
    let currencyForm = documents.querySelector('#currencyForm');
    const initialC = document.querySelector('#initialCurrency').value;
    const finalC = document.querySelector('#finalCurrency').value;
    const amount = document.querySelector('#amount').value;

    // event listener
    document.querySelector('#convertBtn').addEventListener('click', (e) => {
        if(formIsValid(initialC, finalC, amount)) {
            getResult();
        } else alert('error');
    })


}

document.addEventListener("DOMContentLoaded",loaded);