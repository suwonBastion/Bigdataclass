package ClassTV;

public class BrandTV extends TV{

	String brand;
	
	public BrandTV(int intValue, String strValue) {
		// 부모가 가지고 있는 channel 변수에 값을 할당한다.
		super.channel = intValue;
		this.brand = strValue;
	}
	
	public static void main(String args[]) {
		BrandTV objTV = new BrandTV(11, "삼성");
		objTV.channelUp();
		objTV.channelDown();
		System.out.println(objTV.brand + " 현재 채널은" + objTV.channel + "번입니다.");
		
	}
}
