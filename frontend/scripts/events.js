function setUpEvents() {
    var description_title = document.getElementsByTagName("article")[0].getElementsByTagName("h2")[0];


    // description_title.style.textDecoration = "underline"

    description_title.onmouseover = function () {
        description_title.style.textDecoration = "underline";
    };

    description_title.onmouseleave = function () {
        description_title.style.textDecoration = "none";
    };

    // change color of description_title every 3 seconds
    var colors = ["red", "blue", "green", "pink"];
    var index = 0;
    function changeColorOfTitle() {
        if (index === colors.length) {
            index = 0;
        }
        description_title.style.color = colors[index];
        index++;

    }
    var timer = window.setInterval(changeColorOfTitle, 3000);

    description_title.onclick = function () {
        clearInterval(timer);
        // description_title.innerHTML = "WTF MATE!"
        description_title.style.color = "#f87320";
        // alert("You clicked me? Redirecting you to pornhub. Just kidding...");
        // alert("NOT!")
        // window.location.href = "https://www.youtube.com/watch?v=Az5J_EkhYCY&list=PL4cUxeGkcC9i9Ae2D9Ee1RvylH38dKuET&index=43";
    }
}



// another way to do event is through addEvenListener() method
// but we are not going to learn it in this course. 

// window onload events
window.onload = function () {
    // only run these content when the window finishes loading
    // allow you to add <script> tag to head of HTML instead of at 
    // the end of body
    setUpEvents();
    // don't have to do this though, better to just keep script at bottom of body
};