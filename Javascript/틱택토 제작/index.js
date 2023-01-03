let GAME_BOARD = [
    [0, 1, 2,],
    [3, 4, 5,],
    [6, 7, 8,],
];

// 승리 체크 조건
function isWin(x, y) {
    // 1. 플레이어 체크
    //   1-1. 파라미터로 받아서 처리
    //   1-2. 전역변수를 이용해서 처리 ( O )
    // 2. 반복되는 코드를 줄이기
    //   for문을 사용

    // 가로 승리 체크
    // [0 1 2] 
    // [3 4 5] 
    // [6 7 8]
    // 0 을 클릭 -> x = 0; y = 0;
    // 1 을 클릭 -> x = 0; y = 1;
    // 2 를 클릭 -> x = 0; y = 2;
    // GAME_BOARD[0][0] / GAME_BOARD[0][1] / GAME_BOARD[0][2]
    for (let i = 0; i < GAME_BOARD.length; i++) {
        if (GAME_BOARD[x][i] !== player) {
            // 현재 x, i 번째의 값이 player의 모양과 같지 않은 경우
            // 같지 않으면, 다음 모양을 확인할 필요가 없다
            break;
        }
        // 모든 값이 다 같은 경우// i가 2인 경우에도 break를 실행하지 않은 경우
        // i -> 0 1 2 // i는 0부터 시작
        // GAME_BOARD.length = 3 // length는 1부터 셈
        if (i === GAME_BOARD.length - 1) {
            // 가로 승리 !
            return true;
        }
    }

    // 세로 승리 체크
    // [0 1 2] 
    // [3 4 5] 
    // [6 7 8] 
    // 0 을 클릭 -> x = 0; y = 0;
    // 3 을 클릭 -> x = 1; y = 0;
    // 6 을 클릭 -> x = 2; y = 0;
    // 가로: GAME_BOARD[0][0] / GAME_BOARD[0][1] / GAME_BOARD[0][2]
    // 세로: GAME_BOARD[0][0] / GAME_BOARD[1][0] / GAME_BOARD[2][0]
    for (let i = 0; i < GAME_BOARD.length; i++) {
        if (GAME_BOARD[i][y] !== player) {
            break;
        }
        if (i === GAME_BOARD.length - 1) {
            // 세로 승리 !
            return true;
        }
    }

    // 대각선 승리 체크
    // [0 1 2] 
    // [3 4 5] 
    // [6 7 8] 
    // 정대각선 (0, 4, 8)
    // 0 을 클릭 -> x = 0; y = 0;
    // 4 를 클릭 -> x = 1; y = 1;
    // 8 을 클릭 -> x = 2; y = 2;
    // 공통점 = x와 y가 같다
    if (x === y) {
        for (let i = 0; i < GAME_BOARD.length; i++) {
            if (GAME_BOARD[i][i] !== player) {
                break;
            }
            if (i === GAME_BOARD.length - 1) {
                // 정대각선 승리 !
                return true;
            }
        }
    }

    // 역대각선(2, 4, 6)
    // 2 를 클릭 -> x = 0; y = 2;
    // 4 를 클릭 -> x = 1; y = 1;
    // 6 을 클릭 -> x = 2; y = 0;
    // 공통점 x + y === GAME_BOARD.length - 1
    if (x + y === GAME_BOARD.length - 1) {
        for (let i = 0; i < GAME_BOARD.length; i++) {
            // i -> 0, 1, 2
            // y -> 2, 1, 0
            // GAME_BOARD.length - 1 - i;
            // i = 0 -> (GAME_BOARD.length - 1 - i) = 2
            // i = 1 -> (GAME_BOARD.length - 1 - i) = 1
            // i = 2 -> (GAME_BOARD.length - 1 - i) = 0
            // i = 0 -> [0][2]
            // i = 1 -> [1][1]
            // i = 2 -> [2][0]
            if (GAME_BOARD[i][GAME_BOARD.length - 1 - i] !== player) {
                break;
            }
            if (i === GAME_BOARD.length - 1) {
                // 역대각선 승리 !
                return true;
            }
        }
    }
}

// 플레이어 선언
// 플레이어 O 무조건 선
let player = 'O';
let $player = document.createElement('h3');
$player.innerHTML = player + ' 의 차례입니다';
document.body.append($player);

let $buttons = [];

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
        // row = [$button, $button, $button];
        $buttons.push(row);
    }
}

makeGameBoard();

// $buttons = [
//     [$button, $button, $button],
//     [$button, $button, $button],
//     [$button, $button, $button],
// ]
//  GAME_BOARD의 형태와 동일


// 게임 종료 체크
let isGameOver = false;

// 플레이어 차례를 변경해 주는 함수
function changePlayer() {
    // 턴 종료 (플레이어 변경)
    if (player === 'O') {
        player = 'X';
    } else if (player === 'X') {
        player = 'O';
    }

    $player.innerHTML = player + ' 의 차례입니다';
}

// 버튼을 클릭했을때 동작할 함수 선언
// x는 게임판의 몇번째 배열인지 
// y는 x로 찾은 배열의 몇번째 위치인지
// $button은 버튼 엘레먼트
function buttonClick(x, y, $button) {
    if (isGameOver === true) {
        return;
    }

    // 플레이어 체크
    console.log('현재 플레이어', player);

    // 이미 선택된 칸에는 더이상 클릭이 일어나지 않도록 수정
    if (GAME_BOARD[x][y] === 'O' || GAME_BOARD[x][y] === 'X') {
        return;
    }

    // 플레이어 텍스트(O, X) 입력
    $button.innerHTML = player;

    // 게임판에 해당 데이터 저장
    GAME_BOARD[x][y] = player;

    // 승리 체크
    // isWin이 참이라면 (truthy한 값이라면)
    if (isWin(x, y)) {
        // 플레이어 승리 이후 로직
        alert(player + ' 승리 !');

        // 플레이어 텍스트를 승리로 변경
        $player.innerHTML = player + ' 승리!';

        // 승리가 되면 게임 종료
        isGameOver = true;
        // 다시하기 버튼 활성화
        $resetButton.style.visibility = 'visible';
        return; // 함수를 강제 종료
    }

    // 플레이어 변경
    changePlayer();

    // 동작 확인
    console.log(GAME_BOARD);
}

// 게임 재시작 함수
function resetGame() {
    // 게임판 초기화
    GAME_BOARD = [
        [0,1,2],
        [3,4,5],
        [6,7,8]
    ];

    for (let x = 0; x < $buttons.length; x++) {
        for (let y = 0; y < $buttons[x].length; y++) {
            // $button.innerHTML = `게임판: ${x}, ${y}`;
            $buttons[x][y].innerHTML = `게임판: ${x}, ${y}`;
        }
    }

    // 플레이어 초기화
    player = 'O';
    $player.innerHTML = player + ' 의 차례입니다';

    // 게임 종료 여부 초기화
    isGameOver = false;
    $resetButton.style.visibility = 'hidden';
}

// 게임 재시작 버튼
let $resetButton = document.createElement('button');
$resetButton.id = 'reset-btn';
$resetButton.onclick = function() {
    resetGame();
}
$resetButton.innerHTML = '다시하기';
document.body.append($resetButton);
