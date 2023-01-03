// 게임판
let GAME_BOARD = [
    [0, 1, 2,],
    [3, 4, 5,],
    [6, 7, 8,],
];

// 플레이어 선언
let player = 'O';

// 플레이어 텍스트
let $player = document.createElement('h3');
$player.innerHTML = player + ' 의 차례입니다.';

// 게임판 버튼
let $buttons = [];

// 게임 종료 여부
let isGameOver = false;

// 게임 재시작 버튼
let $resetButton = document.createElement('button');
$resetButton.id = 'reset-btn';
$resetButton.innerHTML = '다시하기';
$resetButton.onclick = function() {
    resetGame();
}

// 기타 로직
document.body.append($player);
makeGameBoard();
document.body.append($resetButton);

// 게임판 만들기 함수
function makeGameBoard() {
    for (let x = 0; x < GAME_BOARD.length; x++) {
        let row = [];

        for (let y = 0; y < GAME_BOARD[x].length; y++) {
            // 버튼을 만들기
            let $button = document.createElement('button');
            $button.innerHTML = `게임판: ${x}, ${y}`; // 제가 짠 코드

            // 익명 함수 선언
            // 이렇게 선언된 함수는 익명 함수 라고 함
            // 함수만 받는다. 
            $button.onclick = function() {
                buttonClick(x, y, $button);
            }
            document.body.append($button);
            row.push($button);
        }

        $buttons.push(row);
    }
}

// 버튼 클릭 함수
function buttonClick(x, y, $button) {
    if (isGameOver) {
        return;
    }
    // 플레이어 체크
    console.log('현재 플레이어', player);
    if (GAME_BOARD[x][y] === 'O' || GAME_BOARD[x][y] === 'X') {
        return;
    }

    // 플레이어 텍스트(O, X) 입력
    $button.innerHTML = player;

    // 게임판에 해당 데이터 저장
    GAME_BOARD[x][y] = player;

    // 승리 체크
    if (isWin(x, y)) {
        alert(player + ' 승리!');
        isGameOver = true;
        $resetButton.style.visibility = 'visible';
        $player.innerHTML = player + ' 승리!';
        return;
    }

    changePlayer();

    // 동작 확인
    console.log(GAME_BOARD);
}

// 승리 체크 함수
function isWin(x, y) {
    // 가로 승리 체크
    for (let i = 0; i < GAME_BOARD.length; i++) {
        if (GAME_BOARD[x][i] !== player) {
            break;
        }
        if (i === GAME_BOARD.length - 1) {
            return true;
        }
    }

    // 세로 승리 체크
    for (let i = 0; i < GAME_BOARD.length; i++) {
        if (GAME_BOARD[i][y] !== player) {
            break;
        }
        if (i === GAME_BOARD.length - 1) {
            return true;
        }
    }

    // 대각선 승리 체크
    // 정대각선
    if (x === y) {
        for (let i = 0; i < GAME_BOARD.length; i++) {
            if (GAME_BOARD[i][i] !== player) {
                break;
            }
            if (i === GAME_BOARD.length - 1) {
                return true;
            }
        }
    }

    // 역 대각선
    if (x + y === GAME_BOARD.length - 1) {
        for (let i = 0; i < GAME_BOARD.length; i++) {
            if (GAME_BOARD[i][GAME_BOARD.length - 1 - i] !== player) {
                break;
            }
            if (i === GAME_BOARD.length - 1) {
                return true;
            }
        }
    }
}

// 플레이어 변경 함수
function changePlayer() {
    // 턴 종료 (플레이어 변경)
    if (player === 'O') {
        player = 'X';
    } else if (player === 'X') {
        player = 'O';
    }
    
    $player.innerHTML = player + ' 의 차례입니다.';
}

// 게임 초기화 함수
function resetGame() {
    // 게임판 초기화
    GAME_BOARD = [
        [0, 1, 2,],
        [3, 4, 5,],
        [6, 7, 8,],
    ];

    for (let x = 0; x < $buttons.length; x++) {
        for (let y = 0; y < $buttons[x].length; y++) {
            $buttons[x][y].innerHTML = `게임판: ${x}, ${y}`;
        }
    }

    // 플레이어 초기화
    player = 'O';
    $player.innerHTML = player + ' 의 차례입니다.';

    // 게임 종료 여부 처리
    isGameOver = false;

    // 초기화 버튼 가리기
    $resetButton.style.visibility = 'hidden';
}
