public class TicTacToeMinMax {
    static final int PLAYER_X = 1; // X is maximizer
    static final int PLAYER_O = -1; // O is minimizer
    static final int EMPTY = 0;

    public static void main(String[] args) {
        int[][] board = {
                { 0, 0, 0 },
                { 0, 0, 0 },
                { 0, 0, 0 }
        };

        // Example usage
        int[] bestMove = findBestMove(board, PLAYER_X);
        System.out.println("Best move for X: Row = " + bestMove[0] + ", Col = " + bestMove[1]);
    }

    public static int[] findBestMove(int[][] board, int player) {
        int bestValue = (player == PLAYER_X) ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        int[] bestMove = { -1, -1 };

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) {
                    board[i][j] = player;
                    int moveValue = minimax(board, 0, false, player);
                    board[i][j] = EMPTY;

                    if (player == PLAYER_X && moveValue > bestValue) {
                        bestValue = moveValue;
                        bestMove = new int[] { i, j };
                    } else if (player == PLAYER_O && moveValue < bestValue) {
                        bestValue = moveValue;
                        bestMove = new int[] { i, j };
                    }
                }
            }
        }
        return bestMove;
    }

    public static int minimax(int[][] board, int depth, boolean isMaximizing, int player) {
        int score = evaluate(board);

        if (score == 10 || score == -10 || isFull(board)) {
            return score;
        }

        if (isMaximizing) {
            int best = Integer.MIN_VALUE;

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == EMPTY) {
                        board[i][j] = PLAYER_X;
                        best = Math.max(best, minimax(board, depth + 1, false, player));
                        board[i][j] = EMPTY;
                    }
                }
            }
            return best;
        } else {
            int best = Integer.MAX_VALUE;

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == EMPTY) {
                        board[i][j] = PLAYER_O;
                        best = Math.min(best, minimax(board, depth + 1, true, player));
                        board[i][j] = EMPTY;
                    }
                }
            }
            return best;
        }
    }

    public static int evaluate(int[][] board) {
        for (int row = 0; row < 3; row++) {
            if (board[row][0] == board[row][1] && board[row][1] == board[row][2]) {
                if (board[row][0] == PLAYER_X) return 10;
                if (board[row][0] == PLAYER_O) return -10;
            }
        }

        for (int col = 0; col < 3; col++) {
            if (board[0][col] == board[1][col] && board[1][col] == board[2][col]) {
                if (board[0][col] == PLAYER_X) return 10;
                if (board[0][col] == PLAYER_O) return -10;
            }
        }

        if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            if (board[0][0] == PLAYER_X) return 10;
            if (board[0][0] == PLAYER_O) return -10;
        }

        if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
            if (board[0][2] == PLAYER_X) return 10;
            if (board[0][2] == PLAYER_O) return -10;
        }

        return 0; // No winner
    }

    public static boolean isFull(int[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) return false;
            }
        }
        return true;
    }
}
