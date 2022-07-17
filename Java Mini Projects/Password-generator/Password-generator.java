import java.util.Random;
import java.util.*;  
public class PasswordGenerator 
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);    
        System.out.print("Enter your desired password lenghth: \n");  
        int length= sc.nextInt();  
        System.out.println(length);
        System.out.println(generatePswd(length));
        
    }
    static char[] generatePswd(int len)
    {
        System.out.println("your Secure password is: \n");
        String charscaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String charsmall = "abcdefghijklmnopqrstuvwxyz";
        String nums = "0123456789";
        String symbols = "!@#$%^&*_=+-/€.?<>)";

        String passymbols = charscaps + charsmall + nums + symbols;
        Random rnd = new Random();
        
        char[] pass_word = new char[len];
        int index = 0;
        for (int i = 0; i < len; i++) 
        {
            pass_word[i] = passymbols.charAt(rnd.nextInt(passymbols.length()));
            
        }
        return pass_word;
    }
}
