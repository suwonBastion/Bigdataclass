package ClassTV;

public class BrandTV extends TV{

	String brand;
	
	public BrandTV(int intValue, String strValue) {
		// �θ� ������ �ִ� channel ������ ���� �Ҵ��Ѵ�.
		super.channel = intValue;
		this.brand = strValue;
	}
	
	public static void main(String args[]) {
		BrandTV objTV = new BrandTV(11, "�Ｚ");
		objTV.channelUp();
		objTV.channelDown();
		System.out.println(objTV.brand + " ���� ä����" + objTV.channel + "���Դϴ�.");
		
	}
}
