const header = document.querySelector(".header");
const mobNavToggle = document.querySelector(".mobile-nav-toggle");
const nav = document.querySelector(".navigation");

mobNavToggle.addEventListener("click", () => {
    nav.hasAttribute("data-visible") 
        ? mobNavToggle.setAttribute("aria-expanded", false) 
        : mobNavToggle.setAttribute("aria-expanded", true);
    nav.toggleAttribute("data-visible");
    header.toggleAttribute("data-overlay")
});

const slider = new A11YSlider(document.querySelector('.slider'), {
    adaptiveHeight: false,
    dots: true,
    centerMode: true,
    arrows: false,
    responsive: {
        480: {
          dots: false, // dots enabled 1280px and up
        },
      },
  });