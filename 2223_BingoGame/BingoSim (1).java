public class BingoSim {

    // variables
    private int numCards;
    private boolean[] taken;
    private BingoCard[] cards;

    // constructor
    public BingoSim(int max){
        cards = new BingoCard[max];
        taken = new boolean[15 * 5 + 2];
    }

    //
    public void addCard(BingoCard b){
        cards[numCards++] = b;
    }

    //
    public String simulate(int[] sequence){
        String res = "Simulating ...\n";
        for (int i = 0; i < sequence.length; ++i) {
            int number = sequence[i];
            taken[number] = true;

            for (int cardId = 0; cardId < numCards; ++cardId) {
                cards[cardId].drawn(number);
            }

            char type = 'x';
            if (number <= 15) {
                type = 'B';
            }
            else if (number <= 30) {
                type = 'I';
            }
            else if (number <= 45) {
                type = 'N';
            }
            else if (number <= 60) {
                type = 'G';
            }
            else if (number <= 75) {
                type = 'O';
            }
            else {
                type = '?';
            }

            String state = String.valueOf(i+1) + ". " + type + "-" + String.valueOf(number);
            boolean shouldStop = false;
            for (int cardId = 0; cardId < numCards; ++cardId) {
                int minMove = cards[cardId].minToWin();
                state += " " + String.valueOf(minMove);
                if (minMove == 0) {
                    shouldStop = true;
                }
            }
            res += state + " \n";

            if (shouldStop) {
                break;
            }
        }
        return res;
    }

    //
    public String showCardsWithMin (int min){
        String res = "";
        for (int i = 0; i < numCards; ++i) {
            if (cards[i].minToWin() == min) {
                res += cards[i].toString();
            }
        }
        return res;
    }


    //
    public String toString(){
        String res = " B    I    N    G    O   \n";
        for (int row = 0; row < 15; ++row) {
            String rowData = "";
            for (int col = 0; col < 5; ++col) {
                int num = col * 15 + row + 1;

                if (!taken[num]) {
                    if (num < 10) {
                        rowData += "  " + String.valueOf(num) + "  ";
                    }
                    else {
                        rowData += " " + String.valueOf(num) + "  ";
                    }
                }
                else {
                    if (num < 10) {
                        rowData += "[ " + String.valueOf(num) + "] ";
                    }
                    else {
                        rowData += "[" + String.valueOf(num) + "] ";
                    }
                }
            }
            res += rowData + "\n";
        }

        int drawn = 0;
        for (int i = 0; i < 15 * 5 + 2; ++i) {
            if (taken[i]) {
                drawn++;
            }
        }
        res += "# Drawn: " + String.valueOf(drawn)  + "\n";

        res += "mins:";
        int numWinners = 0;
        for (int i = 0; i < numCards; ++i) {
            int minMoves = cards[i].minToWin();
            res += String.valueOf(minMoves) + " ";

            if (minMoves == 0) {
                numWinners++;
            }
        }

        res += "\n# Winners: " + String.valueOf(numWinners) + " out of " + String.valueOf(numCards);

        return res;
    }
}
