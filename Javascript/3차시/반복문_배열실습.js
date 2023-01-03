// 빈 배열에 1부터 10까지의 숫자 넣기
// 배열에 값을 넣는 방법
// 1. 배열 인덱스에 직접 넣는 법
// 2. push()를 이용해 넣는 방법

// 1. 배열 인덱스에 직접 넣는 법
let array = [];
for (let i = 0; i < 10; i++) {
    array[i] = i + 1;
}

console.log(array);

// 2. push()를 이용해 넣는 방법
let array2 = [];
for (let i = 1; i <= 100; i++) {
    array2.push(i);

    if (i == 10) {
        break;
    }
}
console.log(array2);