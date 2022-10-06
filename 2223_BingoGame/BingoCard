public class BingoCard {

    // variables
    private int[][] card;
    private boolean[][] taken;
    public static final int[] MY_WINNER = {7,1,3,4,5,20,23,16,29,17,32,38,39,40,46,47,48,49,52,73,68,69,70,71};//{7,20,32,46,73,1,23,38,47,68,3,16,48,52,4, 29, 39, 49, 53, 5,17,40,50,54};

    // constructor - no return value
    public BingoCard(int[] data) {
        card = new int[5][5];
        taken = new boolean[5][5];

        int d = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!(i == 2 && j == 2)) {
                    card[j][i] = data[d++];
                }
            }
        }
        taken[2][2] = true; //by default is F int ==0
    }

    // check valid values
    public boolean isValid() {
        boolean[] vis = new boolean[15 * 5 + 2];
        for (int col = 0; col < 5; ++col) {
            for (int row = 0; row < 5; ++row) {
                if (row == 2 && col == 2) {
                    continue;
                }

                int val = card[row][col];
                if ( !(15 * col < val && val <= 15 * (col + 1)) || vis[val] ) {
                    return false;
                }
                vis[val] = true;
            }
        }
        return true;
    }

    // update numbers
    public void drawn(int number) {
        // System.out.println("T_T: " + number);
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!(i == 2 && j == 2)) {
                    if (number == card[i][j]) {
                        taken[i][j] = true; // say number, update array
                        return; // dont need to check the rest of value
                    }
                }
            }
        }
    }

    public void drawn(int[] numbers) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (!(i == 2 && j == 2)) {
                    for (int k = 0; k < numbers.length; k++) {
                        if (numbers[k] == card[i][j]) {
                            taken[i][j] = true; // say number, update array
                            break; // dont need to check the rest of value
                        }
                    }
                }
            }
        }
    }

    public void reset() {
        // card = new int[5][5];
        taken = new boolean[5][5];
        taken[2][2] = true;
    }

    public boolean isAWinner() {
        // horizontal
        for (int row = 0; row < 5; ++row) {
            boolean winnable = true;
            for (int col = 0; col < 5; ++col) {
                if (!taken[row][col]) {
                    winnable = false;
                    break;
                }
            }
            if (winnable) {
                return true;
            }
        }

        // vertical
        for (int col = 0; col < 5; ++col) {
            boolean winnable = true;
            for (int row = 0; row < 5; ++row) {
                if (!taken[row][col]) {
                    winnable = false;
                    break;
                }
            }
            if (winnable) {
                return true;
            }
        }

        /* primary diagonal */ {
            boolean winnable = true;
            for (int d = 0; d < 5; ++d) {
                if (!taken[d][d]) {
                    winnable = false;
                    break;
                }
            }
            if (winnable) {
                return true;
            }
        }

        /* secondary digonal */ {
            boolean winnable = true;
            for (int d = 0; d < 5; ++d) {
                if (!taken[d][4-d]) {
                    winnable = false;
                    break;
                }
            }
            if (winnable) {
                return true;
            }
        }

        // check MY_WINNER
        for (int i = 0; i < MY_WINNER.length; ++i) {
            int val = MY_WINNER[i];
            boolean ok = false;
            for (int row = 0; row < 5; ++row) {
                if (ok) {
                    break;
                }
                for (int col = 0; col < 5; ++col) {
                    if (card[row][col] == val) {
                        ok = true;
                        break;
                    }
                }
            }
            if (!ok) {
                return false;
            }
        }

        return true;
    }

    // number of numbers left to win the game
    public int minToWin() {
        int minCells = 4;

        /* horizontal */ {
            for (int row = 0; row < 5; ++row) {
                int notTakenCells = 0;
                for (int col = 0; col < 5; ++col) {
                    if (!taken[row][col]) {
                        notTakenCells++;
                    }
                }
                minCells = Math.min(minCells, notTakenCells);
            }
        }

        /* vertical */ {
            for (int col = 0; col < 5; ++col) {
                int notTakenCells = 0;
                for (int row = 0; row < 5; ++row) {
                    if (!taken[row][col]) {
                        notTakenCells++;
                    }
                }
                minCells = Math.min(minCells, notTakenCells);
            }
        }

        /* primary diagonal */ {
            int notTakenCells = 0;
            for (int d = 0; d < 5; ++d) {
                if (!taken[d][d]) {
                    notTakenCells++;
                }
            }
            minCells = Math.min(minCells, notTakenCells);
        }

        /* secondary digonal */ {
            int notTakenCells = 0;
            for (int d = 0; d < 5; ++d) {
                if (!taken[d][4-d]) {
                    notTakenCells++;
                }
            }
            minCells = Math.min(minCells, notTakenCells);
        }

        return minCells;
    }

    // interface
    public String toString(){
        String res = " B    I    N    G    O   \n";
        for (int row = 0; row < 5; ++row) {
            String rowData = "";
            for (int col = 0; col < 5; ++col) {
                if (row == 2 && col == 2) {
                    rowData += "[FR] ";
                    continue;
                }

                if (!taken[row][col]) {
                    if (card[row][col] < 10) {
                        rowData += "  " + String.valueOf(card[row][col]) + "  ";
                    }
                    else {
                        rowData += " " + String.valueOf(card[row][col]) + "  ";
                    }
                }
                else {
                    if (card[row][col] < 10) {
                        rowData += "[ " + String.valueOf(card[row][col]) + "] ";
                    }
                    else {
                        rowData += "[" + String.valueOf(card[row][col]) + "] ";
                    }
                }
            }
            res += rowData + "\n";
        }
        return res;
    }
}
