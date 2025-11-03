// Mobile Menu
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');
menuToggle.addEventListener('click', () => navLinks.classList.toggle('active'));
document.querySelectorAll('.nav-item').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.contains('active') && navLinks.classList.remove('active'));
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Paw Reveal
document.querySelectorAll('.paw-reveal').forEach((char, i) => {
  char.style.setProperty('--i', i);
});

// Particle System (Reduced particles for performance)
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let particles = [];

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

class Particle {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = canvas.height + 50;
    this.size = Math.random() * 20 + 15;
    this.speedX = Math.random() * 1 - 0.5;
    this.speedY = Math.random() * 2 + 1;
    this.type = Math.random() > 0.5 ? 'Paw' : 'Bone';
  }
  update() {
    this.x += this.speedX;
    this.y -= this.speedY;
    if (this.y < -50) {
      this.y = canvas.height + 50;
      this.x = Math.random() * canvas.width;
    }
  }
  draw() {
    ctx.font = `${this.size}px serif`;
    ctx.fillStyle = 'rgba(255,255,255,0.4)';
    ctx.fillText(this.type, this.x, this.y);
  }
}

function init() { particles = []; for (let i = 0; i < 30; i++) particles.push(new Particle()); }  // Reduced from 50
function animate() { ctx.clearRect(0, 0, canvas.width, canvas.height); particles.forEach(p => { p.update(); p.draw(); }); requestAnimationFrame(animate); }
init(); animate();

// Bark Sound
setTimeout(() => {
  document.getElementById('barkSound').volume = 0.3;
  document.getElementById('barkSound').play().catch(() => {});
}, 1000);

// Dark Mode Toggle
document.getElementById('darkModeToggle').addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  fetch('/toggle_dark_mode', { method: 'POST' });  // Save preference (add route if needed)
});