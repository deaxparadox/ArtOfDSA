package algorithms.search;

import java.util.Arrays;

public class BinarySearch {
    public static int rank(int key, int[] a) {
        // Array must be sorted
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi)
        {
            // Key is in a[lo..hi] or not present.
            int mid = lo + (hi - lo) /  2;
            if (key < a[mid]) { hi = mid - 1;}
            else if (key > a[mid]) { lo = mid + 1;}
            else { return mid; }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] whitelist = {23, 45, 12, 99, 4, 8, 19, 56, 73, 28};

        // Original Array
        System.out.print("Original Array: ");
        for (int i=0; i<whitelist.length; i++) {
            System.out.print(whitelist[i] + ", ");
        }
        System.out.println();

        // Sorting array
        Arrays.sort(whitelist);

        // print sorted array
        System.out.print("Sorted Array: ");
        for (int i=0; i<whitelist.length; i++) {
            System.out.print(whitelist[i] + ", ");
        }
        System.out.println();

        int key = 19;
        int index = BinarySearch.rank(key, whitelist);
        System.out.println("Index of " + key + " is " + index);
    }
}
