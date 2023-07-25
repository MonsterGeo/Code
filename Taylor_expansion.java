package calculus;

public class Taylor_expansion {
	//示例代码是e^x在x=0处的20阶泰勒展开
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		double sum = 0; //初始化求和
		double sumlist=0;//定义20前的级数求和
		
		for(int i=1;i<=20;i++) {
			double k = factorial(i);
			sum = 1/k+sumlist;
			sumlist = sum;
		}
		System.out.println("e^x在0处的20阶泰勒展开为："+sum);
	}
	
	
	//阶乘，用来定义泰勒展开的
	public static double factorial(int n) {
		if(n==1) {
			return 1;
		}else {
			return n*factorial(n-1);
		}
	}

}
