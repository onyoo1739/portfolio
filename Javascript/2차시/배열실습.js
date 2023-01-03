// 사과, 배, 오렌지 순으로 저장된 fruits 배열 만들기
let fruits = ['사과', '배', '오렌지'];

// 배를 포도로 바꾸기
fruits[1] = '포도';

// fruits 배열 마지막에 바나나 추가하기
fruits.push('바나나');

// fruits 배열 제일 앞에 수박 추가하기
fruits.unshift('수박');

// fruits 배열 제일 마지막 요소 제거하기
fruits.pop();

// fruits 배열 요소의 갯수 출력하기
console.log(fruits.length);