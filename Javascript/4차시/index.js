// 입력받은 x의 n 제곱을 반환해주는 함수 작성
function pow(x, n) {
    // return x ** n;
    let multi = 1;
    for(let i = 1; i <= n; i++) {
        multi = multi * x;
    }
    return multi;
}

console.log(pow(3, 2)); // 9
console.log(pow(2, 10)); // 1024

// 입력받은 두 숫자 중 작은 값을 반환해주는 함수 작성
function min(a, b) {
    // let a; // 이렇게는 사용 불가 !
    // let b; // 파라미터의 이름과 선언하는 변수명은 겹치면 안된다 ! 
    if (a > b) {
        return b;
    } else if (a === b || a < b) {
        return a;
    }
}

console.log(min(10, 5)); // 5
console.log(min(1, -5)); // -5
