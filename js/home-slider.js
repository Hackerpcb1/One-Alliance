document.addEventListener("DOMContentLoaded", function () {
  const slider = document.querySelector("[data-oa-home-slider]");
  if (!slider) return;

  const slides = Array.from(slider.querySelectorAll(".oa-home-slide"));
  const dots = Array.from(slider.querySelectorAll(".oa-home-slider__dot"));
  let activeIndex = slides.findIndex((slide) => slide.classList.contains("is-active"));
  let timerId;

  if (activeIndex < 0) activeIndex = 0;

  function showSlide(index) {
    activeIndex = (index + slides.length) % slides.length;

    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle("is-active", slideIndex === activeIndex);
      slide.setAttribute("aria-hidden", slideIndex === activeIndex ? "false" : "true");
    });

    dots.forEach((dot, dotIndex) => {
      dot.classList.toggle("is-active", dotIndex === activeIndex);
      dot.setAttribute("aria-pressed", dotIndex === activeIndex ? "true" : "false");
    });
  }

  function startTimer() {
    window.clearInterval(timerId);
    timerId = window.setInterval(() => showSlide(activeIndex + 1), 6500);
  }

  dots.forEach((dot, index) => {
    dot.addEventListener("click", () => {
      showSlide(index);
      startTimer();
    });
  });

  showSlide(activeIndex);
  startTimer();
});
