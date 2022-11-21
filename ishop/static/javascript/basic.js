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


function productCalculate(id, operator){

    add_btn = document.getElementById('add_btn' + id);
    result_div = document.getElementById('result_div' + id);

    value = Number(add_btn.getAttribute('value'));
    new_value = 1;

    if (operator == "+"){
        new_value =  value + 1;
    }

    if (operator == "-"){
        new_value = value > 2 ? value - 1 : 1;
    }

    add_btn.setAttribute('value', new_value);
    result_div.textContent = new_value;

}


function updateCart(id, operator) {

    qty_input = document.getElementById('qty_input' + id);
    qty = Number(qty_input.getAttribute('value'));

    if (operator == "+"){
        qty = qty + 1;
    }

    if (operator == "-"){
        qty = qty > 1 ? qty - 1 : 0;
    }

    qty_input.setAttribute('value', qty);
    document.getElementById('qty_div' + id).textContent = qty;

    document.getElementById('updatecart'+id).submit();
}
