var items = document.getElementsByClassName("item")

for (var i = 0; i < items.length; i++) {
    items[i].addEventListener('click', play, false);
}

function play(el) {
    var req = new XMLHttpRequest();
    const url = new URL(window.location.href)
    const path = url.pathname + el.target.innerText;

    req.onreadystatechange = function() {
        if (this.readyState == 4) {
            console.log(req.response);
        }
    };

    req.open('GET', url.origin + '/play' + path, true);
    req.send();
};

console.log('Hi There!')
