/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
		/*int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[0]);
		int c = Integer.parseInt(args[0]);
		*/
		System.out.println("Hello World");
		
		double r =0, r1=0;
		int i =0;
		for(i=0;i<5;i++){
		    r = Math.random();
		    System.out.println(r);
		    System.out.println(Math.min(r,r1));
		    System.out.println(Math.max(r,r1));
		    r1=r;
		}
		
		//swap
		r = 3;
		r1 =4;
		//System.out.println("Before exchange");
		System.out.println(r);
		System.out.println(r1);
		
		//System.out.println("After exchange");
		double t =0;
		t =r; //3
		
		r=r1; //4
		r1=t; //3
		System.out.println(r);
		System.out.println(r1);
		
		//Flip
		if (Math.random() < 0.5)
            System.out.println("Heads");
        else
            System.out.println("Tails");

		//sort
		r = 33;
		r1 =4;
		//System.out.println("Before sort");
		System.out.println(r);
		System.out.println(r1);
		
		//System.out.println("After sort");
		if (r1 < r){
    		double t1 =0;
    		t1 =r; //3
    		
    		r=r1; //4
    		r1=t1; //3
		}
		System.out.println(r);
		System.out.println(r1);
		
		//while loo[p] - powers of 2
		i = 0;
        int v = 1, n=10;
        while (i <= n)
        {
             System.out.println(v);
             i = i + 1;
             v = 2 * v;
        } 
         
        //sqrt
        double EPS = 1E-15;
        double c = 46;//Double.parseDouble(args[0]);
        t = c;
        while (Math.abs(t - c/t) > t*EPS)
            t = (c/t + t) / 2.0;
        System.out.println(t); 

        //tax
        double income = 120000;//Double.parseDouble(args[0]);
        double rate = 0.35;
        if (income < 47450) rate = 0.22;
        if (income >= 114650) rate = 0.25;
        if (income >= 174700) rate = 0.28;
        if (income >= 311950) rate = 0.33;
        System.out.println(rate); 
    
        //Large Factors - StackTraceElement
        long n1 = 3757208;//Long.parseLong(args[0]);
        for ( i = 2; i <= n1/i; i++) //<n1 will take more time
        {
            while (n1 % i == 0)
            {
                System.out.print(i + " ");
                n1 = n1 / i;
            }
            if (n1> 1) 
                System.out.println("TRACE " + i + " " + n1);
            else  
                System.out.println();
        }
        
        int a3 = 2;
        int b3 = 3;
        int c3 = 4;
        if (a3 < b3){
            if (b3 < c3)
            {
                if (c3 < a3) System.out.println(a3 + " " + b3 + " " + c3);
                else System.out.println(c3 + " " + b3 + " " + a3);
            }
            else System.out.println(a3 + " " + c3 + " " + b3);
        }
        else 
            System.out.println(b3 + " " + a3 + " " + c3);
        //a = 0;
        //c = c/a;

        //put deck of cards in order
        {
            String[] rank = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" };
            String[] suit = { "♣", "♦", "♥", "♠" };
            String[] deck = new String[52];
            for (int j = 0; j < 4; j++)
                for (i = 0; i < 13; i++)
                    deck[i + 13*j] = rank[i] + suit[j];
            
            for (i = 0; i < 52; i++)
                System.out.print(deck[i] + " ");
            System.out.println();

            //change order
            for (i = 0; i < 13; i++)
                for (int j = 0; j < 4; j++)
                    deck[i + 13*j] = rank[i] + suit[j];
            
            for ( i = 0; i < 52; i++)
                System.out.print(deck[i] + " ");
            System.out.println();

            //Deck to put the cards in rank order in the array
            for ( i = 0; i < 13; i++)
                for (int j = 0; j < 4; j++)
                    deck[4*i + j] = rank[i] + suit[j];
            for ( i = 0; i < 52; i++)
                System.out.print(deck[i] + " ");
            
            System.out.println();

            int N =5;
            //take a card, any card
            for (i = 0; i < N; i++)
            {
                int r2 = (int) (Math.random() * 52);
                System.out.println(deck[r2]);
            }  
            
            //shuffle the deck
            for (i = 0; i < 52; i++)
            {
                int r2 = (int) (Math.random() * 52);
                String t2 = deck[r2];
                deck[r2] = deck[i];
                deck[i] = t2;
            }
            //take a card, any card
            for (i = 0; i < N; i++)
                System.out.println(deck[i]);

            //shuffle the deck of 10 cards
            for (i = 0; i < 10; i++)
            {
                int r2 = (int) (Math.random() * 52);
                String t2 = deck[r2];
                deck[r2] = deck[i];
                deck[i] = t2;
            }
            //take a card, any card
            for (i = 0; i < 10; i++)
                System.out.println(deck[i]);

            //matrix addition
            int[][] aa = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
            int[][] bb = { { 9, 8, 7 }, { 6, 5, 4 }, { 3, 2, 1 } };
            int[][] cc = new int[3][3];
            for (i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    cc[i][j] = aa[i][j] + bb[i][j];   
            double[][] c4 = new double[3][3];
            for ( i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    c4[i][j] = aa[i][j] + bb[i][j];

            //matrix multiplication
            for ( i = 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    cc[i][j] = aa[i][0]*bb[0][j] + aa[i][1]*bb[1][j] + aa[i][2]*bb[2][j];
            for(i= 0; i < 3; i++)
                for (int j = 0; j < 3; j++)
                    for (int k = 0; k < 3; k++)
                        cc[i][j] += aa[i][k] * bb[k][j]; 
        } 

        n = 123456;
        int m = 0;
        while (n != 0)
        {
            m = (10 * m) + (n % 10);
            n = n / 10;
        }
        System.out.println(m);

        int j;
        for ( i = 0, j = 0; i < 10; i++)
            j += i;
        System.out.println(j);

        //math
        int a1 = 90;//Integer.parseInt(args[0]); 
        int b1 = 45;//Integer.parseInt(args[1]); 
        int sum  = a1 + b1; 
        int prod = a1 * b1; 
        int quot = a1 / b1; 
        int rem  = a1 % b1; 
        System.out.println(a1 + " + " + b1 + " = " + sum); 
        System.out.println(a1 + " * " + b1 + " = " + prod); 
        System.out.println(a1 + " / " + b1 + " = " + quot); 
        System.out.println(a1 + " % " + b1 + " = " + rem); 
      
        //quadratic
        // Parse coefficients from command-line. 
        double b2 = 45.2;//Double.parseDouble(args[0]); 
        double c2 = 35.7;//Double.parseDouble(args[1]); 

        // Calculate roots of x*x + b*x + c. 
        double discriminant = b2*b2 - 4.0*c2; 
        double d = Math.sqrt(discriminant); 
        double root1 = (-b2 + d) / 2.0; 
        double root2 = (-b2 - d) / 2.0; 
        // Print them out. 
        System.out.println(root1); 
        System.out.println(root2); 
      
        //leap year
        int year = 1942;//Integer.parseInt(args[0]); 
        boolean isLeapYear;

        // divisible by 4 but not 100 
        isLeapYear = (year % 4 == 0) && (year % 100 != 0); 
        // or divisible by 400 
        isLeapYear = isLeapYear || (year % 400 == 0); 
        System.out.println(isLeapYear); 

		//double sqrt(double c, double eps) 
        { 
            double c=23.2,eps=3.0;
            if (c < 0) c=0;//return Double.NaN; 
            double t = c; 
            while (Math.abs(t - c/t) > eps * t) 
               t = (c/t + t) / 2.0; 
            //return t; 
            System.out.println(t);
            System.out.println(sqrt(c,eps));
        }
        maths_random();
        System.out.println(cube(6));
        System.out.println(pdf(3.0));
        System.out.println(pdf(3.0,3.0,4));
        System.out.println(cdf(3.0));
        System.out.println(cdf(3.0,3.0,4));
        System.out.println(max3(3.0,3.0,4));
        System.out.println(max3(3,3,4));
        System.out.println(lg(16));

        int[] ha = {0,1,2,2,4,5,6,7,8,9};
        int hm = 10; 
        int[] hist = histogram(ha,hm);
        for (int i = 0; i < hm; i++)
            System.out.println(i + " " + hist[i]);      
    
        {
            // Example data: generate 1000 random numbers between 0 and 1
            int[] data = new int[10];
            for (int i = 0; i < data.length; i++) {
                data[i] = ha[i];//Math.random();
            }

            // Call the histogram function
            histogram(data, 10);  // 10 bins
        }
        longestRun(ha);
        filter(ha);
        sortAndRemoveDuplicates(ha);
        signalAnalysis(new double[]{-0.5, 0.2, -0.1, 0.4, -0.3, 0.1, -0.2, 0.3, -0.4, 0.5});
    }
    public static double sqrt(double c, double eps)  
    { 
        if (c < 0) return Double.NaN; 
        double t = c; 
        while (Math.abs(t - c/t) > eps * t) 
            t = (c/t + t) / 2.0; 
        return t; 
    } 

    public static int cube(int i) 
    { 
        int j = i * i * i; 
        return j; 
    }   

    //Gaussian distribution
    public static double cdf1(double x) 
    {   
        double sum = 0.0, term = x, k = 1.0; 
        while (Math.abs(term) > 1E-15) 
        {   
            sum += term; 
            term *= x*x / k; 
            k += 2.0; 
        } 
        return 0.5 + sum * pdf(x); 
    }

    public static double cdf1(double x, double mu, double sigma) 
    {   
        return cdf1((x - mu) / sigma); 
    }

    public static double cdf(double z) 
    { 
       if (z < -8.0) return 0.0; 
       if (z >  8.0) return 1.0; 
       double sum = 0.0, term = z; 
       for (int i = 3; sum + term != sum; i += 2) 
       { 
          sum  = sum + term; 
          term = term * z * z / i; 
       } 
       return 0.5 + sum * pdf(z); 
    } 
    
    public static double cdf(double z, double mu, double sigma) 
    {  return cdf((z - mu) / sigma);  }


    public static double pdf(double x) 
    {   
        return Math.exp(-x*x / 2) / Math.sqrt(2 * Math.PI); 
    } 
    public static double pdf(double x, double mu, double sigma) 
    {   
        return pdf((x - mu) / sigma)/sigma; 
    } 

    //max of 3 numbers
    public static int max3(int a, int b, int c) {
        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;
        return max;
    }

    public static double max3(double a, double b, double c) {
        double max = a;
        if (b > max) max = b;
        if (c > max) max = c;
        return max;
    }
    /*1.2.30 Uniform random numbers. Write a program that prints five uniform random numbers between 0 and 1, their average 
    value, and their minimum and maximum values. Use Math.random(), Math.min(), and Math.max().
    */
       public static void maths_random() {
        double[] numbers = new double[5];
        double sum = 0;
        double min = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;

        // Generate five uniform random numbers between 0 and 1
        for (int i = 0; i < 5; i++) {
            numbers[i] = Math.random();
            sum += numbers[i];
            min = Math.min(min, numbers[i]);
            max = Math.max(max, numbers[i]);
        }

        double average = sum / 5;

        // Print the results
        System.out.println("Five uniform random numbers:");
        for (double num : numbers) {
            System.out.printf("%.6f ", num);
        }
        System.out.println();
        System.out.printf("Average: %.4f\n", average);
        System.out.printf("Minimum: %.4f\n", max);
        System.out.printf("Maximum: %.4f\n", min);
    }

    //2.1.10 Write a static method lg() that takes an int argument n and returns the largest integer not larger than the base-2 logarithm of n. Do not use the Math library.
    public static int lg(int n) {
        int log = 0;
        while (n >= 2) {
            n /= 2;
            log++;
        }
        return log;
    }

    //2.1.19 Write a static method histogram() that takes an int array a[] and an integer m as arguments and returns an array of length m whose ith element is the number of times the integer i appeared in a[]. Assuming the values in a[] are all between 0 and m-1, the sum of the values in the returned array should equal a.length.
    public static int[] histogram(int[] a, int m) {
        int[] hist = new int[m];
        for (int value : a) {
            if (value >= 0 && value < m) {
                hist[value]++;
            }
        }
        return hist;
    }

    //1.5.5 Write a program that reads in a sequence of integers and prints both the integer that appears in a longest consecutive run and the length of that run. For example, if the input is 1 2 2 1 5 1 1 7 7 7 7 1 1, then your program should print Longest run: 4 consecutive 7s.
    final int MAX_SIZE = 1000;
    public static void longestRun(int[] a) {    
        int longestRunLength = 1;
        int longestRunValue = a[0];
        int currentRunLength = 1;

        for (int i = 1; i < a.length; i++) {
            if (a[i] == a[i - 1]) {
                currentRunLength++;
            } else {
                if (currentRunLength > longestRunLength) {
                    longestRunLength = currentRunLength;
                    longestRunValue = a[i - 1];
                }
                currentRunLength = 1;
            }
        }

        // Check at the end of the array
        if (currentRunLength > longestRunLength) {
            longestRunLength = currentRunLength;
            longestRunValue = a[a.length - 1];
        }

        System.out.println("Longest run: " + longestRunLength + " consecutive " + longestRunValue + "s.");
    }

    //1.5.6 Write a filter that reads in a sequence of integers and prints the integers, removing repeated values that appear consecutively. For example, if the input is 1 2 2 1 5 1 1 7 7 7 7 1 1 1 1 1 1 1 1 1, your program should print 1 2 1 5 1 7 1. 
    public static void filter(int[] a) {
        for (int i = 0; i < a.length; i++) {
            if (i == 0 || a[i] != a[i - 1]) {
                System.out.print(a[i] + " ");
            }
        }
        System.out.println();
    }

    //1.5.7 Write a program that reads in a sequence of integers and prints the integers in sorted order, removing duplicates. For example, if the input is 1 2 2 1 5 1 1 7 7 7 7 1 1, your program should print 1 2 5 7.
    public static void sortAndRemoveDuplicates(int[] a) { 
        java.util.Arrays.sort(a);
        for (int i = 0; i < a.length; i++) {
            if (i == 0 || a[i] != a[i - 1]) {
                System.out.print(a[i] + " ");
            }
        }
        System.out.println();
    }
    //1.5.7 Write a program that reads in a sequence of integers and prints the integers in sorted order, removing duplicates. For example, if the input is 1 2 2 1 5 1 1 7 7 7 7 1 1, your program should print 1 2 5 7.
    /*for (int i = 0; i < a.length; i++) {
        if (i == 0 || a[i] != a[i - 1]) {
            System.out.print(a[i] + " ");
        }
    }*/

   /*
   1.5.17 Write a program that reads in a sequence of real numbers between -1 and +1 and prints their average magnitude, average power, and the number of zero crossings. The average magnitude is the average of the absolute values of the data values. The average power is the average of the squares of the data values. The number of zero crossings is the number of times a data value transitions from a strictly negative number to a strictly positive number, or vice versa. These three statistics are widely used to analyze digital signals.
   */
   final int MAX_SIZE = 1000;
   public static void signalAnalysis(double[] a) {  
        double sumMagnitude = 0.0;
        double sumPower = 0.0;
        int zeroCrossings = 0;

        for (int i = 0; i < a.length; i++) {
            sumMagnitude += Math.abs(a[i]);
            sumPower += a[i] * a[i];
            if (i > 0 && ((a[i] > 0 && a[i - 1] < 0) || (a[i] < 0 && a[i - 1] > 0))) {
                zeroCrossings++;
            }
        }

        double averageMagnitude = sumMagnitude / a.length;
        double averagePower = sumPower / a.length;

        System.out.printf("Average Magnitude: %.4f\n", averageMagnitude);
        System.out.printf("Average Power: %.4f\n", averagePower);
        System.out.println("Number of Zero Crossings: " + zeroCrossings);
    }        
}
