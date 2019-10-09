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

///About Animation Scrolling
const aboutText = document.querySelector('.about-text');
const aboutImage = document.querySelector('.img-post');
const about = document.querySelector('#about');

const aboutOptions = {
	rootMargin: '200px 0px 0px 0px'
};

const aboutObserver = new IntersectionObserver(function(entries, aboutObserver) {
	entries.forEach((entry) => {
		if (entry.isIntersecting) {
			aboutText.classList.add('text-anime');
			aboutImage.classList.add('image-file');
		} else {
			aboutText.classList.remove('text-anime');
			aboutImage.classList.remove('image-file');
		}
	});
}, aboutOptions);
aboutObserver.observe(about);

/// Progress Bar scroling animation
// const proBar = document.querySelector('#progress');
const skillScroll = document.querySelector('#skills');

const skillOptions = {
	rootMargin: '280px 0px 0px 0px'
};
const skillObserver = new IntersectionObserver(function(entries, skillObserver) {
	entries.forEach((entry) => {
		if (entry.isIntersecting) {
			$('.progress-bar').each(function() {
				$(this).find('.progress-content').animate(
					{
						width: $(this).attr('data-percentage')
					},
					3000
				);

				$(this).find('.progress-number-mark').animate(
					{ left: $(this).attr('data-percentage') },
					{
						duration: 3000,
						step: function(now, fx) {
							var data = Math.round(now);
							$(this).find('.percent').html(data + '%');
						}
					}
				);
			});
		} else {
			$('.progress-bar').each(function() {
				$(this).find('.progress-content').animate(
					{
						width: 0
					},
					0
				);

				$(this).find('.progress-number-mark').animate(
					{ left: 0 },
					{
						duration: 0,
						step: function(now, fx) {
							var data = Math.round(now);
							$(this).find('.percent').html(0 + '%');
						}
					}
				);
			});
		}
	});
}, skillOptions);
skillObserver.observe(skillScroll);

// CLIENT SLIDER
var slideIndex = 0;
showSlides(slideIndex);

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

// GOOGLE MAP API
var map;

function initMap() {
	var options = {
		center: { lat: 25.91047, lng: -80.1076339 },
		zoom: 10
		// mapTypeId: google.maps.MapTypeId.HYBRID
	};
	map = new google.maps.Map(document.getElementById('googlemap'), options);
}

// function initMap() {
// 	// The location of Uluru
// 	var latLng = { lat: 25.91047, lng: -80.1076339 };
// 	// The map, centered at Uluru
// 	var map = new google.maps.Map(document.getElementById('googlemap'), { zoom: 4, center: latLng });
// 	// The marker, positioned at Uluru
// 	var marker = new google.maps.Marker({ position: latLng, map: map });
// }
