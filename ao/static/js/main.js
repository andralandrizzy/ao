$(document).ready(function() {
	$('.sidenav').sidenav();
	M.updateTextFields();
});
// Navbar Color Change
const nav = document.querySelector('.main-nav');
const mainBody = document.querySelector('main');

const mainOptions = {
	rootMargin: '0px 0px -180px 0px'
};
const mainObserver = new IntersectionObserver(function(entries, mainObserver) {
	entries.forEach((entry) => {
		if (!entry.isIntersecting) {
			nav.classList.add('transparent');
		} else {
			nav.classList.remove('transparent');
		}
	});
}, mainOptions);
mainObserver.observe(mainBody);

//Progress bar
$(document).ready(function() {
	$('.progress-bar').each(function() {
		$(this).find('.progress-content').animate(
			{
				width: $(this).attr('data-percentage')
			},
			2000
		);

		$(this).find('.progress-number-mark').animate(
			{ left: $(this).attr('data-percentage') },
			{
				duration: 2000,
				step: function(now, fx) {
					var data = Math.round(now);
					$(this).find('.percent').html(data + '%');
				}
			}
		);
	});
});

// CLIENT SLIDER
var slideIndex = 0;

function showSlides() {
	var i;
	var slides = document.getElementsByClassName('client-testimonial-content');
	var dots = document.getElementsByClassName('dot');
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = 'none';
	}
	slideIndex++;
	if (slideIndex > slides.length) {
		slideIndex = 1;
	}
	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(' active', '');
	}
	slides[slideIndex - 1].style.display = 'block';
	dots[slideIndex - 1].className += ' active';
	setTimeout(showSlides, 6000); // Change image every 2 seconds
}

// Alert messages fade out
setTimeout(function() {
	$('#message').fadeOut('slow');
}, 6000);

// TESTIMONIAL MODAL FORM
// Testimonial modal
var modal = document.querySelector('#formModal');

// Get the button that opens the modal
var testimonialBtn = document.querySelector('#testBtn');

// Get the <span> element that closes the modal
var span = document.querySelector('.modal-close');

// When the user clicks the button, open the modal

testimonialBtn.addEventListener('click', function styleDisplay() {
	modal.style.display = 'block';
});

// When the user clicks on <span> (x), close the modal
span.addEventListener('click', function closeBtn() {
	modal.style.display = 'none';
});

// // When the user clicks anywhere outside of the modal, close it

window.addEventListener('click', function closeBtn(e) {
	if (e.target == modal) {
		modal.style.display = 'none';
	}
});
