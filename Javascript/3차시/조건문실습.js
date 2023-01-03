let user = prompt('당신은 누구입니까?');

if (user == null) {
    alert('취소되었습니다')
} else if (user != 'Admin') {
    alert('인증되지 않은 사용자 입니다')
} else if (user == 'Admin') {
    let password = prompt('비밀번호를 입력하세요')

    if (password == null) {
        alert('취소되었습니다')
    } else if (password != 'Master') {
        alert('인증 실패')
    } else if (password == 'Master') {
        alert('환영합니다')
    }
}