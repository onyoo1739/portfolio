const h1 = document.querySelector('h1');
const body = document.body;

const {width, height} = h1.getBoundingClientRect();

let currentLeft = h1.getBoundingClientRect().left;
let currentTop = h1.getBoundingClientRect().top;

const position = ['right', 'bottom'];

function move() {
  const speed = 2;
  const rect = body.getBoundingClientRect();
  if (currentLeft  < 0) position[0] = 'right';
  if (currentLeft + width > rect.width) position[0] = 'left';
  if (currentTop + height >= rect.height) position[1] = 'top';
  if (currentTop <= 0) position[1] = 'bottom';


  if (position[0] === 'left') {
    currentLeft -= speed;
    h1.style.left = currentLeft + 'px';
  }
  if (position[0] === 'right') {
    currentLeft += speed;
    h1.style.left = currentLeft + 'px';
  }
  if (position[1] === 'bottom') {
    currentTop += speed;
    h1.style.top = currentTop + 'px';
  }
  if (position[1] === 'top') {
    currentTop -= speed;
    h1.style.top = currentTop + 'px';
  }


  requestAnimationFrame(move);
}

requestAnimationFrame(move)
document.addEventListener('resize', () => requestAnimationFrame(move));