import java.util.Scanner;
public class swapnibble {
    public static int swap_nibble(int x){
        return ((x & 0x0F) <<4 | (x & 0xF0) >>4);
    }

     public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        System.out.println(swap_nibble(x));
        sc.close();
        
    }
}
