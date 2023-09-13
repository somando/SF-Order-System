function opencloseBarcode() {

    const element = document.getElementById('scanner-element');
    const buttonId = document.getElementById('opencloseButtonBar');

    if (element.style.display == 'none') {
        element.style.display = 'block';
        buttonId.innerHTML = 'Close';
    } else {
        element.style.display = 'none';
        buttonId.innerHTML = 'Open';
    }

}

function opencloseDiscount() {

    const element = document.getElementById('discountPriceContent');
    const buttonId = document.getElementById('opencloseButtonDis');

    if (element.style.display == 'none') {
        element.style.display = 'block';
        buttonId.innerHTML = 'Close';
    } else {
        element.style.display = 'none';
        buttonId.innerHTML = 'Open';
    }

}

function rotate() {

    const element = document.getElementById('regiPrice');

    if (element.classList.contains('norotate')) {
        element.classList.add('rotate');
        element.classList.remove('norotate');
    } else {
        element.classList.add('norotate');
        element.classList.remove('rotate');
    }

}

function change() {

    const deposit = Number(document.getElementById('deposit').value);
    const depositRow = document.getElementById('depositRow');
    const depositTable = document.getElementById('depositTable');
    const price = document.getElementById('regiPriceNum');
    const price_value = Number(document.getElementById('priceValue').value);
    const name = document.getElementById('modeName');
    const submitPay = document.getElementById('submitPay')

    if (deposit >= price_value) {
        submitPay.removeAttribute('disabled');
    } else {
        submitPay.setAttribute('disabled', true);
    }

    depositRow.style.display = 'table-row';
    name.innerHTML = 'Change';
    depositTable.innerHTML = deposit.toLocaleString() + ' 円';
    price.innerHTML = (deposit - price_value).toLocaleString();

}