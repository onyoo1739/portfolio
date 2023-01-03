function 로그인() {
    // 아이디
    // $가 앞에 나온 변수는 HTML Element를 저장하는구나
    // 라는 암묵적인 규칙
    let $id = document.getElementById('user-id');
    // 비밀번호
    let $password = document.getElementById('password');

    console.log($id);
    console.log($password);

    // input에 사용자가 입력한 값은 value 라고 하는 프로퍼티에 저장
    let id = $id.value;
    let password = $password.value;

    console.log(id);
    console.log(password);

    // 로그인 기능 구현
    if (id === 'nunch.dev' || id === 'admin') {
        if (password == '1q2w3e4r!!@@@@') {
            alert('로그인 되었습니다');
        } else {
            alert('로그인 실패 !');
        }
    } else {
        alert('로그인 실패 !');
    }

    // 로그인 성공시 성공 텍스트 출력
    let $h1 = document.createElement('h1');
    $h1.innerHTML = '로그인 성공!!';
    document.body.append($h1);
}
