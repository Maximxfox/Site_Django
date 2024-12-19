const slides = document.querySelector('.slides');
const images = document.querySelectorAll('.slides img');
let currentIndex = 0;

document.getElementById('next').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
});

document.getElementById('prev').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
});