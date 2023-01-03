let 점수 = +prompt('점수를 입력하세요');

if (점수 >= 90) {
// 90 이상 A
    console.log('A');
} else if (점수 >= 80 && 점수 < 90) {
// 80 ~ 90 B
    console.log('B');
} else if (점수 >= 70 && 점수 < 80) {
// 70 ~ 80 C
    console.log('C');
} else {
// ~ 70 F
    console.log('F');
}

// --------------------------------

// 1부터 10까지의 합을 구하라

let sum = 0;
for( let i = 1; i <= 10 ; i++ ) {
    sum = sum + i;
}

console.log(sum); // 55

