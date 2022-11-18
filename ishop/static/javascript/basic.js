/* Image Slider in productDetails page */
const wrapper = document.querySelector('.cards-wrapper');
const dots = document.querySelectorAll('.dot');
let activeDotNum = 0;

dots.forEach((dot, idx) => {
    dot.setAttribute('data-num', idx);
    dot.addEventListener('click', (e) => {

        let clickedDotNum = e.target.dataset.num;
        if (clickedDotNum == activeDotNum) {
            return;
        }
        else {
            let displayArea = wrapper.parentElement.clientWidth;
            let pixels = -displayArea * clickedDotNum;
            wrapper.style.transform = 'translateX(' + pixels + 'px)';
            dots[activeDotNum].classList.remove('active');
            dots[clickedDotNum].classList.add('active');
            activeDotNum = clickedDotNum;
        }

    });
});

/* Navbar Dropdown */
   

    $('a.dropdown-toggle').click(function () {
        if (!$(this).next().hasClass('show')) {
            $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
        }
        var $subMenu = $(this).next(".dropdown-menu");
        $subMenu.toggleClass('show');


        $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function (e) {
            $('.dropdown-submenu .show').removeClass("show");
        });   
    });
 
