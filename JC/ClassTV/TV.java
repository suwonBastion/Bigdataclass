package ClassTV;

public class TV {

	int channel;

// ����Ʈ ������
public TV() {}


// ������
public TV(int intValue) {
	this. channel = intValue;
	
}

protected void channelUp() {
	channel = channel +1;
}

private void channelDown() {
	channel = channel - 1;
	if (channel < 0) {
		channel = 0;
	}
}

public static void main(String args[]) {
	TV objTV = new TV(11);
	System.out.println("���� ä���� " + objTV.channel + "���Դϴ�.");
 }
}