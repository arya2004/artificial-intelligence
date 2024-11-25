import java.util.*;

public class TicTacToeGame{
    
    static final int PLAYER_X = 1;
    static final int PLAYER_O = -1;
    static final int EMPTY = 0;

    public static void main(String[] args){
        
        int[][] board = {
            {0,0,0},
            {0,0,0},
            {0,0,0}
        };

        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Tic-Tac-Toe!");
        System.out.println("You are 'O' (Minimizer), and the computer is 'PLAYER_X' (Maximizer).");
        printBoard(board);

        while (true) {
            System.out.println("your move");
            int row = scanner.nextInt();
            int col = scanner.nextInt();

            if(board[row][col] != EMPTY){
                System.out.println("wrong move try again");
                continue;
                
            }

            board[row][col] = PLAYER_O;
            printBoard(board);

            if(evaluate(board) == -10){
                System.out.println("you win");
                break;  
            }else if(isFull(board)){
                System.out.println("draw");
                break;
            }  

            //computer turn
            int[] bestMove = findBestMove(board, PLAYER_X);

        }


    }


    public static int[] findBestMove(int[][] board, int player){

        int[] bestMove = {-1, -1};
        int bestValue = Integer.MAX_VALUE;
        if(player == PLAYER_X) bestValue = Integer.MIN_VALUE;

        for(int i =0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(board[i][j] == EMPTY){
                    board[i][j] = player;
                    int moveValue = miniMax(board, 0, false, player);
                    board[i][j] = EMPTY;

                    if(player == PLAYER_X && moveValue > bestValue){
                        bestValue = moveValue;
                        bestMove = new int[] { i, j};
                    }else if(player == PLAYER_O && moveValue < bestValue){
                        bestValue = moveValue;
                        bestMove = new int[] {i, j};
                    }


                }
            }
        }


        return bestMove;
    }

    public static int miniMax(int[][] board, int depth, boolean isMaximizing, int player){
        
        int score = evaluate(board);

        if(score == 10 || score == -1 || isFull(board)){
            return score;
        }  

        if(isMaximizing){

            int best = Integer.MIN_VALUE;

            for(int i = 0; i < 3; i++){
                for(int  j = 0; j < 3; j++){
                    if(board[i][j] == EMPTY){
                        board[i][j] = PLAYER_X;
                        best = Math.max(best, miniMax(board, depth + 1, false, player));
                        board[i][j] = EMPTY;
                    }
                }
            }

            return best;

        }else {

            int best = Integer.MAX_VALUE;

            for(int i = 0; i < 3; i++){
                for(int  j = 0; j < 3; j++){
                    if(board[i][j] == EMPTY){
                        board[i][j] = PLAYER_O;
                        best = Math.max(best, miniMax(board, depth + 1, true, player));
                        board[i][j] = EMPTY;
                    }
                }
            }

            return best;

        }



       

    }


    public static boolean isFull(int[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == EMPTY) return false;
            }
        }
        return true;
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

    public static void printBoard(int [][] board){
        for(int i = 0; i< 3; i++){
            for(int j = 0; j < 3; j++){
                if(board[i][j] == PLAYER_X){
                    System.out.print("X ");
                }else if(board[i][j] == PLAYER_O){
                    System.out.print("O ");
                }else{
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

}