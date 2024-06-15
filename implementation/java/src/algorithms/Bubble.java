package algorithms;

public class Bubble {
    private int[] array;
    private int length;
    public Bubble(int arr[]) {
        if (arr == null) {
            System.out.println("Cannot work in empty array");
            System.exit(1);
        }
        array = arr;
        length = array.length;
    }
    public void sort() {
        for (int i=0; i<length; i++) {
            boolean swapped = false;

            for (int j=0; j<length-i-1; j++) {
                if (array[j] > array[j+1]) {
                    int temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) {
                break;
            }
        }
    }

    public void show() {
        if (array == null) {
            System.err.println("Cannot print and emtpy array!");
        }
        for (int i=0; i<length; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.println();
    }

    public  static void main(String args[]) {
        int[] array = {12, 34, 23, 65, 5, 9, 11};
        Bubble b = new Bubble(array);
        System.out.print("Original Array: ");
        b.show();
        b.sort();
        System.out.print("Sorted Array: ");
        b.show();
    }
}
