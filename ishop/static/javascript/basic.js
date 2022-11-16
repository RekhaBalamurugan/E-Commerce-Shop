
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