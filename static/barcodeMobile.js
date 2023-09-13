Quagga.init({
  locate: true,
  inputStream:{
    name:"Live",
    type:"LiveStream",
    constraints: {
      facingMode: 'environment'
    },
    target: document.querySelector('#barcode-scanner'),
  },
  decoder: {
    readers : [
      "code_39_reader", 
      "code_39_vin_reader"
    ],
    multiple: false
  },
  locator: {
    halfSample: false,
    patchSize: "medium"
  }
}, function(err) {
  if (err) {
    console.log(err);
    return;
  }
  
  //バーコードをスキャンできた際のイベント
  Quagga.onDetected((data)=> {
    const code_value = data.codeResult.code;
    document.getElementById('barcode').value = code_value;
  });

  Quagga.start();
});