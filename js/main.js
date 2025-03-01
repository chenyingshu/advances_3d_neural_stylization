/*********************** Comparison Slider *****************************/
/* Modified from
 https://medium.com/@predragdavidovic10/native-dual-range-slider-html-css-javascript-91e778134816
 https://www.codehim.com/html5-css3/html-css-image-comparison-slider/
 by Yingshu Chen
* */

$(document).ready(function () {
    // new Dics({
    //     container: document.querySelector("#disc-slider"),
    //     textPosition: "top"
    // });

    // Navbar
    let scrollerBlock = $("#navbarSection");
    let fromAbstract = document.querySelector('#tldr');

    $(window).scroll(function () {
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

function updateImages() {
    leftValue = fromSlider.value;
    rightValue = toSlider.value;
    // console.log("from:",leftValue);
    // console.log("to:",rightValue);
    imagesComp[0].style.clipPath = "polygon(0% 0%, " + leftValue + "% 0%, " + leftValue + "% 100%, 0% 100%)";
    imagesComp[1].style.clipPath = "polygon(0% 0%, " + rightValue + "% 0%, " + rightValue + "% 100%, 0% 100%)";
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
    const rangeDistance = to.max - to.min;
    const fromPosition = from.value - to.min;
    const toPosition = to.value - to.min;
    controlSlider.style.background = `linear-gradient(
      to right,
      ${sliderColor} 0%,
      ${sliderColor} ${(fromPosition) / (rangeDistance) * 100}%,
      ${rangeColor} ${((fromPosition) / (rangeDistance)) * 100}%,
      ${rangeColor} ${(toPosition) / (rangeDistance) * 100}%, 
      ${sliderColor} ${(toPosition) / (rangeDistance) * 100}%, 
      ${sliderColor} 100%)`;
}

function setToggleAccessible(currentTarget) {
    const toSlider = document.querySelector('#toSlider');
    if (Number(currentTarget.value) <= 0) {
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

document.addEventListener("DOMContentLoaded", function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

function createCard(card) {
    return `
    <div class="col mb-4">
      <div class="card h-100">
        <div class="card-body">
          <h6 class="card-title">${card.title}</h6>
          <p class="card-text">${card.conference}</p>
          ${card.tags.map(tag => `
            <button type="button" class="btn ${tag.class}" disabled>${tag.text}</button>
          `).join("")}
        </div>
        <div class="card-footer">
          ${Object.entries(card.links).map(([type, url]) => {
        let iconClass;
        switch (type) {
            case "paper":
                iconClass = "fas fa-file-alt";
                break;
            case "code":
                iconClass = "fab fa-github";
                break;
            case "project":
                iconClass = "fas fa-pager";
                break;
            default:
                iconClass = "";
        }
        return `
              <a href="${url}" class="figure-group-vertical" target="_blank" data-toggle="tooltip" title="View ${type.charAt(0).toUpperCase() + type.slice(1)}">
                <i class="${iconClass} figure-img logo-label"></i>
              </a>
            `;
    }).join("")}
        </div>
      </div>
    </div>
  `;
}

async function renderCards() {
    try {
        // Fetch the JSON file
        const response = await fetch('js/paper_data.json'); // Path to your JSON file
        if (!response.ok) {
            throw new Error('Failed to load card data');
        }

        // Parse the JSON data
        const cardData = await response.json();

        // Get the container element
        const container = document.querySelector(".row.row-cols-1.row-cols-md-3");
        if (!container) {
            console.error("Container element not found!");
            return;
        }

        // Clear the container
        container.innerHTML = "";

        // Get all active tags
        const activeTags = Array.from(document.querySelectorAll('.selector-container .btn[aria-pressed="true"]'))
            .map(button => button.textContent.trim()); // Get the text content of active buttons

        // If no tags are active, hide all items
        if (activeTags.length === 0) {
            return;
        }

        // Filter JSON items based on active tags
        const filteredCards = cardData.filter(card => {
            // Check if the card has tags that match all active tags
            return activeTags.every(activeTag =>
                card.tags.some(tag => tag.text === activeTag)
            );
        });

        // Render matching cards
        filteredCards.forEach(card => {
            const cardHtml = createCard(card);
            container.insertAdjacentHTML("beforeend", cardHtml);
        });

        // Initialize Bootstrap tooltips
        $(document).ready(function () {
            $('[data-toggle="tooltip"]').tooltip();
        });
    } catch (error) {
        console.error("Error loading or rendering cards:", error);
    }
}

// Function to add event listeners to buttons
function setupButtonListeners() {
    // Get all buttons under .selector-container
    const buttons = document.querySelectorAll('.selector-container .btn');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Get the parent group of the clicked button
            const parentGroup = button.closest('.button-group');

            // Check if the button belongs to the "3D Representation" or "Optimization Type" group
            const groupHeading = parentGroup.querySelector('h4').textContent.trim();
            const isSingleActiveGroup = groupHeading === '3D Representation' || groupHeading === 'Optimization Type';

            if (isSingleActiveGroup) {
                // Deactivate all other buttons in the same group
                parentGroup.querySelectorAll('.btn').forEach(otherButton => {
                    if (otherButton !== button) {
                        otherButton.setAttribute('aria-pressed', 'false');
                        otherButton.classList.remove('active'); // Remove the 'active' class for css
                    }
                });
            }

            // Toggle the clicked button's active state
            // const isPressed = button.getAttribute('aria-pressed') === 'true';
            // button.setAttribute('aria-pressed', !isPressed);

            // Toggle the 'active' class for the clicked button
            // button.classList.toggle('active', !isPressed);

            // Re-render cards based on the updated active tags
            renderCards();
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    renderCards();
    setupButtonListeners();
})
