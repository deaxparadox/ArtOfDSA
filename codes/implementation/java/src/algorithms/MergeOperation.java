package algorithms;

import java.util.Arrays;

public class MergeOperation {

    public static int[] mergeArray(int[] a, int[] b) {
        int alen = a.length;
        int blen = b.length;
        int clen = alen+blen;
        int[] c = new int[clen];

        int ai = 0;
        int bi = 0;
        int ci = 0;

        while ((ai < alen) && (bi < blen)) {
            if (a[ai] < b[bi]) {
                c[ci] = a[ai];
                ci++;
                ai++;
            } else {
                c[ci] = b[bi];
                ci++;
                bi++;
            }
        }


        while (ai < alen) {
            c[ci] = a[ai];
            ci++;
            ai++;
        }

        while (bi < blen) {
            c[ci] = b[bi];
            ci++;
            bi++;
        }
        return c;
    }


    public  static void main(String[] args) {
        int[] a = {34, 1, 8, 19, 99};
        int[] b = {23, 45, 91, 22, 102};

        Arrays.sort(a);
        Arrays.sort(b);

        int[] c = MergeOperation.mergeArray(a, b);
        System.out.print("Merged Sorted Array: ");
        for (int i=0; i<c.length; i++) {
            System.out.print(c[i] + ", ");
        }
    }

}


