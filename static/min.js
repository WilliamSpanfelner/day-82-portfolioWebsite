console.log("Rock and roll!")

document.querySelectorAll('.nav-link').forEach
(link => {
    if(link.href === window.location.href) {
        link.setAttribute('aria-current', 'page')
        link.setAttribute('class', 'nav-link active')
    }
})