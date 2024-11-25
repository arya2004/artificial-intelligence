

import java.util.*;

public class Random {
    static char[][] board = {
            {' ', ' ', ' '},
            {' ', ' ', ' '},
            {' ', ' ', ' '}
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        boolean playerTurn = true;
        boolean gameWon = false;
        char winner = ' ';

        printBoard();

        for (int i = 0; i < 9; i++) {
            if (playerTurn) {
                System.out.println("Player's turn (enter position 1-9): ");
                int pos = scanner.nextInt() - 1;

                int row = pos / 3;
                int col = pos % 3;

                if (board[row][col] == ' ') {
                    board[row][col] = 'X';
                    playerTurn = false;
                } else {
                    System.out.println("Cell already taken. Try again.");
                    i--;
                }
            } else {
                if (i == 0 && board[1][1] == ' ') {  // Computer's first move
                    board[1][1] = 'O';
                } else if (!tryToWin()) {  // Try to win
                    int pos, row, col;
                    do {
                        pos = random.nextInt(9);
                        row = pos / 3;
                        col = pos % 3;
                    } while (board[row][col] != ' ');

                    board[row][col] = 'O';
                }
                playerTurn = true;
            }

            printBoard();
            winner = checkWinner();
            if (winner != ' ') {
                gameWon = true;
                break;
            }
        }

        if (gameWon) {
            System.out.println("Game over! Winner is " + winner);
        } else {
            System.out.println("Game over! It's a draw.");
        }

        scanner.close();
    }

    public static boolean tryToWin() {
        // Check rows and columns for a win
        for (int i = 0; i < 3; i++) {
            // Rows
            if (board[i][0] == 'O' && board[i][1] == 'O' && board[i][2] == ' ') {
                board[i][2] = 'O';
                return true;
            }
            if (board[i][0] == 'O' && board[i][2] == 'O' && board[i][1] == ' ') {
                board[i][1] = 'O';
                return true;
            }
            if (board[i][1] == 'O' && board[i][2] == 'O' && board[i][0] == ' ') {
                board[i][0] = 'O';
                return true;
            }
            // Columns
            if (board[0][i] == 'O' && board[1][i] == 'O' && board[2][i] == ' ') {
                board[2][i] = 'O';
                return true;
            }
            if (board[0][i] == 'O' && board[2][i] == 'O' && board[1][i] == ' ') {
                board[1][i] = 'O';
                return true;
            }
            if (board[1][i] == 'O' && board[2][i] == 'O' && board[0][i] == ' ') {
                board[0][i] = 'O';
                return true;
            }
        }

        // Check diagonals for a win
        if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == ' ') {
            board[2][2] = 'O';
            return true;
        }
        if (board[0][0] == 'O' && board[2][2] == 'O' && board[1][1] == ' ') {
            board[1][1] = 'O';
            return true;
        }
        if (board[1][1] == 'O' && board[2][2] == 'O' && board[0][0] == ' ') {
            board[0][0] = 'O';
            return true;
        }
        if (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == ' ') {
            board[2][0] = 'O';
            return true;
        }
        if (board[0][2] == 'O' && board[2][0] == 'O' && board[1][1] == ' ') {
            board[1][1] = 'O';
            return true;
        }
        if (board[1][1] == 'O' && board[2][0] == 'O' && board[0][2] == ' ') {
            public class Random {
    
            }
            board[0][2] = 'O';
            return true;
        }

        return false;
    }

    public static void printBoard() {
        System.out.println("Current board:");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j]);
                if (j < 2) System.out.print("|");
            }
            System.out.println();
            if (i < 2) System.out.println("-----");
        }
    }

    public static char checkWinner() {
        // Check rows and columns
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') {
                return board[i][0];
            }
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ') {
                return board[0][i];
            }
        }

        // Check diagonals
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') {
            return board[0][0];
        }
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ') {
            return board[0][2];
        }

        return ' ';
    }
}
