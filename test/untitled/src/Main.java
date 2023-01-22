public class Main {
    public static void main(String[] args) {
        char c = 'a';
        for (int i = 0, j = 1, k = 0; i < 26 + 3; i ++, ++ k) {
            System.out.printf("%c ", (char) (c + i));
            if (k == j) {
                System.out.println();
                k = 0;
                j ++;
            }
        }
    }
}