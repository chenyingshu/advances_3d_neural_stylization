/*********************** Comparison Slider *****************************/
/* Modified from
 https://medium.com/@predragdavidovic10/native-dual-range-slider-html-css-javascript-91e778134816
 https://www.codehim.com/html5-css3/html-css-image-comparison-slider/
 by Yingshu Chen
* */


$(document).ready(function()  {
    // new Dics({
    //     container: document.querySelector("#disc-slider"),
    //     textPosition: "top"
    // });

    // Navbar
    let scrollerBlock = $("#navbarSection");
    let fromAbstract = document.querySelector('#tldr');

    $(window).scroll(function() {
        if ($(this).scrollTop() > fromAbstract.offsetTop) {
            scrollerBlock.fadeIn(400);
        } else {
            scrollerBlock.fadeOut(400);
        }
    });

    $(document).click(function (event) {
        var clickover = $(event.target);
        var $navbar = $(".navbar-collapse");
        var _opened = $navbar.hasClass("show");
        if (_opened === true && !clickover.hasClass("navbar-toggle")) {
            $navbar.collapse('hide');
        }
    });

    // Sliders
    const fromSlider = document.querySelector('#fromSlider');
    const toSlider = document.querySelector('#toSlider');
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    setToggleAccessible(toSlider);

    fromSlider.oninput = () => controlFromSlider(fromSlider, toSlider);
    toSlider.oninput = () => controlToSlider(fromSlider, toSlider);

    // Images (support three image now only)
    const imageCompIds = ['goldenComp', 'nightComp', 'milkywayComp'];
    imagesComp = [];
    for (let i = 0; i < imageCompIds.length; i++) {
        imagesComp.push(document.getElementById(imageCompIds[i]));
    }

});

function updateImages(){
    leftValue = fromSlider.value;
    rightValue = toSlider.value;
    // console.log("from:",leftValue);
    // console.log("to:",rightValue);
    imagesComp[0].style.clipPath = "polygon(0% 0%, "+leftValue+"% 0%, "+leftValue+"% 100%, 0% 100%)";
    imagesComp[1].style.clipPath = "polygon(0% 0%, "+rightValue+"% 0%, "+rightValue+"% 100%, 0% 100%)";
}
function controlFromSlider(fromSlider, toSlider) {
    const [from, to] = getParsed(fromSlider, toSlider);
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    if (from > to) {
        fromSlider.value = to;
    }
    updateImages();
}

function controlToSlider(fromSlider, toSlider) {
    const [from, to] = getParsed(fromSlider, toSlider);
    // fillSlider(fromSlider, toSlider, '#C6C6C6', '#25daa5', toSlider);
    setToggleAccessible(toSlider);
    if (from <= to) {
        toSlider.value = to;
    } else {
        toSlider.value = from;
    }
    updateImages();
}

function getParsed(currentFrom, currentTo) {
    const from = parseInt(currentFrom.value, 10);
    const to = parseInt(currentTo.value, 10);
    return [from, to];
}

function fillSlider(from, to, sliderColor, rangeColor, controlSlider) {
    const rangeDistance = to.max-to.min;
    const fromPosition = from.value - to.min;
    const toPosition = to.value - to.min;
    controlSlider.style.background = `linear-gradient(
      to right,
      ${sliderColor} 0%,
      ${sliderColor} ${(fromPosition)/(rangeDistance)*100}%,
      ${rangeColor} ${((fromPosition)/(rangeDistance))*100}%,
      ${rangeColor} ${(toPosition)/(rangeDistance)*100}%, 
      ${sliderColor} ${(toPosition)/(rangeDistance)*100}%, 
      ${sliderColor} 100%)`;
}

function setToggleAccessible(currentTarget) {
    const toSlider = document.querySelector('#toSlider');
    if (Number(currentTarget.value) <= 0 ) {
        toSlider.style.zIndex = 2;
    } else {
        toSlider.style.zIndex = 0;
    }
}

function copyCitation() {
    /* Copy text into clipboard */
    text_data = document.getElementById('citationText').textContent;
    navigator.clipboard.writeText(text_data);
    var tooltip = document.getElementById("copyTooltip");
    tooltip.innerHTML = "Copied!";
}

function resetTooltip() {
    var tooltip = document.getElementById("copyTooltip");
    tooltip.innerHTML = "Copy";
}
