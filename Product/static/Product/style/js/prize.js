function generatetoken() {

    var random = Math.floor(Math.random() * 100);

    if (random == 0) {
        document.getElementById('prizeAmt').value = random;
        document.getElementById("res").innerHTML = 'You won Rs 50 recharge';
        console.log("first");
    } else if (random > 10 && random < 30) {
        document.getElementById('prizeAmt').value = random;
        document.getElementById("res").innerHTML = ' You won Rs 10 recharge';
        console.log("second");


    } else if (random > 50 && random < 55) {
        document.getElementById('prizeAmt').value = random;
        document.getElementById("res").innerHTML = ' You won Rs 20 recharge';
        console.log("Third");

    } else if (random == 60) {
        document.getElementById('prizeAmt').value = random;
        document.getElementById("res").innerHTML = ' You won Rs 20 recharge';
        console.log("Fourth");

    } else {
        document.getElementById('prizeAmt').value = random;
        document.getElementById("res").innerHTML = ' You won Rs 20 recharge';
        console.log("Fifth");
    }
}