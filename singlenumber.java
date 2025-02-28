import java.util.Scanner;
public class singlenumber{
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;  // XOR cancels out duplicates
        }
        return result;
    }
}

