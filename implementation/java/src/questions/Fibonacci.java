package questions;

public class Fibonacci {
    private static long calculate1(int num ) {
        if (num == 0) {
            return 0;
        }
        if (num == 1) {
            return 1;
        }
        return calculate1(num-1) + calculate1(num-2);
    }
    public static void calculate_recur(int num) {
        long total = calculate1(num);
        System.out.println("Fibonacci of " + num + " is " + total);
    }

    public static void main(String[] args) {
        boolean hour = false;
        int count = 1;
        int pre_count = 0;
        long start = 0;
        long end = 0;
        int time = 0;
        int total_time = 0;
        int time_hour_in_seconds = 3600;
        while (!hour) {
//            if (count == 60) { break; }
            start = System.currentTimeMillis();
            Fibonacci.calculate_recur(count);
            end = System.currentTimeMillis();
            time = (int) (end-start)/1000;
            total_time += time;

            if (time > time_hour_in_seconds) {
                System.out.println("Time exceeds 1h\n");

                System.out.println("Largest value which can be");
                System.out.println("calculated in 1 hour in java: " + pre_count);
                break;
            }
            System.out.println("Time " + time + "s; Total time: "+ total_time + "s\n");
            pre_count = count;
            count++;
        }
    }
}
