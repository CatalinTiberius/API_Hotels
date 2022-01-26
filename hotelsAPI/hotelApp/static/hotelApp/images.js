window.onload = function() {
    var images = document.querySelectorAll("img");
    images.forEach(image => {
        let oldsrc = image.src;
        let newsrc = oldsrc.slice(-oldsrc.length, -14);
        image.src = newsrc + "y.jpg";
        console.log(newsrc);
    });
}