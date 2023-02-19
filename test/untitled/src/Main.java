public class Main {
    public static void main(String[] args) {
        char c = 'a';
        for (int i = 0, j = 1, k = 0; i < 26 + 3; i ++, ++ k) {
            System.out.printf("%c ", (char) (c + i));
            if (k == j) {
                tuki();
                k = 0;
                j ++;
            }
        }
    }

    private static void tuki() {
        System.out.println();
    }
}