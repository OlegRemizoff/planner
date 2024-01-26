var navLinks = document.querySelectorAll("nav a");
for (var i = 0; i < navLinks.length; i++) {
	var link = navLinks[i]
	if (link.getAttribute('href') == window.location.pathname) {
		link.classList.add("live");
		break;
	}
}


// $(document) .ready(function () {

//     $('.navCol a').each(function(){
//         let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
//         let link = this.href;
//         if(location == link){
//             console.log(link)
//             // $(this).parent().addClass('active');
//             $(this).addClass('active');
//         }
//     });