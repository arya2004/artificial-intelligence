import java.util.*;

public class CryptarithmeticSolver {

    // Store the unique letters
    private static char[] letters;
    // Map letters to digits
    private static int[] letterToDigit;
    
    private static boolean[] usedDigits;
    // Store words in the left expression
    private static String[] leftWords;
    // Store the right expression (the sum)
    private static String rightWord;
  
    private static Set<Character> leadingLetters;

    public static void main(String[] args) {
        
        String input = "JAVA+JAVA=MONEY".replaceAll("\\s+", "");

   
        if (!parseInput(input)) {
            System.out.println("Invalid input format.");
            return;
        }

     
        Set<Character> letterSet = new HashSet<>();
        leadingLetters = new HashSet<>();
        for (String word : leftWords) {
            for (char c : word.toCharArray()) {
                letterSet.add(c);
            }
            leadingLetters.add(word.charAt(0));
        }
        for (char c : rightWord.toCharArray()) {
            letterSet.add(c);
        }
        leadingLetters.add(rightWord.charAt(0));

        if (letterSet.size() > 10) {
            System.out.println("Too many unique letters; cannot solve with digits 0-9.");
            return;
        }

        letters = new char[letterSet.size()];
        int idx = 0;
        for (char c : letterSet) {
            letters[idx++] = c;
        }

        letterToDigit = new int[letters.length];
        Arrays.fill(letterToDigit, -1);
        usedDigits = new boolean[10];

      
        if (!solve(0)) {
            System.out.println("No solution found.");
        }
    }

 
    private static boolean parseInput(String input) {
        String[] sides = input.split("=");
        if (sides.length != 2) {
            return false;
        }
        leftWords = sides[0].split("\\+");
        rightWord = sides[1];
        return true;
    }

  
    private static boolean solve(int pos) {
        if (pos == letters.length) {
      
            if (isValidSolution()) {
                printSolution();
                return true; 
            }
            return false;
        }

        for (int digit = 0; digit <= 9; digit++) {
            if (usedDigits[digit]) {
                continue;
            }
   
            if (digit == 0 && leadingLetters.contains(letters[pos])) {
                continue;
            }
            usedDigits[digit] = true;
            letterToDigit[pos] = digit;
            if (solve(pos + 1)) {
                return true; // Return true to find one solution
            }
            usedDigits[digit] = false;
            letterToDigit[pos] = -1;
        }
        return false;
    }

   
    private static boolean isValidSolution() {
        long leftSum = 0;
        for (String word : leftWords) {
            long num = wordToNumber(word);
            if (num == -1) {
                return false; // Leading zero detected
            }
            leftSum += num;
        }
        long rightNum = wordToNumber(rightWord);
        if (rightNum == -1) {
            return false;
        }
        return leftSum == rightNum;
    }

   
    private static long wordToNumber(String word) {
        long num = 0;
        for (char c : word.toCharArray()) {
            int digit = letterToDigit[letterIndex(c)];
            if (digit == -1) {
                return -1; 
            }
            num = num * 10 + digit;
        }
        // Check for leading zero
        if (num > 0 && Long.toString(num).length() != word.length()) {
            return -1;
        }
        return num;
    }

  
    private static int letterIndex(char c) {
        for (int i = 0; i < letters.length; i++) {
            if (letters[i] == c) {
                return i;
            }
        }
        return -1;
    }

  
    private static void printSolution() {
        System.out.println("Solution found:");
        for (int i = 0; i < letters.length; i++) {
            System.out.println(letters[i] + " = " + letterToDigit[i]);
        }
        System.out.println("Verification:");
        for (int i = 0; i < leftWords.length; i++) {
            System.out.print(wordToNumber(leftWords[i]));
            if (i < leftWords.length - 1) {
                System.out.print(" + ");
            }
        }
        System.out.print(" = " + wordToNumber(rightWord));
        System.out.println();
    }
}
