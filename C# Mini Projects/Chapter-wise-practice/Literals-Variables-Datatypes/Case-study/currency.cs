using System;
public class currency{
    static void Main(string[] args){
        Console.WriteLine("Enter your amount: ");
        string number = Console.ReadLine(); // taking input as string
        int num;
        num = Convert.ToInt32(number); // converting input as integer
        double dollarvalue = (double)num*79.4;
        double poundvalue = (double)num*83.2;
        
        Console.WriteLine("****Currency Convertor****");
        Console.WriteLine("\n\nCurrency data formatted using # character\n");
        Console.WriteLine("Rupee Amount: {0,0:Rs ###.##}",num);
        Console.WriteLine("Dollar Amount : {0,0:$ ###.##}",dollarvalue);
        Console.WriteLine("Pound Amount : {0,0:pd ###.##}",poundvalue);
        Console.WriteLine("\n\nCurrency data formatted using . character\n");
        Console.WriteLine("Rupee Amount:{0,0:Rs 000.00} ",num);
        Console.WriteLine("Dollar Amount : {0,0:$ 000.00} \n",dollarvalue);
        Console.WriteLine("Pound Amount : {0,0:pd 000.00} ",poundvalue);
        Console.WriteLine("\n\nCurrency data formatted using , character\n");
        Console.WriteLine("Rupee Amount: {0,0:Rs 000,00}",num);
        Console.WriteLine("Dollar Amount : {0,0:$ 0,000.00}",dollarvalue);
        Console.WriteLine("Pound Amount : {0,0:pd 0,000.00}",poundvalue);
    }
}
