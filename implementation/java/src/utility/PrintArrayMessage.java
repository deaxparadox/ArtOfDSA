package utility;

public class PrintArrayMessage {
    public static void print(int[] arr, String[] message) {
        System.out.print(message);
        int arrlen = arr.length;
        for (int i=0; i<arrlen; i++) {
            if (i == arrlen-1) {
                System.out.println(arr[i]);
            } else {
                System.out.print(arr[i] + ", ");
            }
        }
    }
}
