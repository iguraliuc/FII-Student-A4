import java.awt.List;
import java.util.ArrayList;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Register 
{
	public static String[] username= {"tudor.manoleasa", "marian_cretu" ,"@!-/>23" ,"123" ,".....","الْأَبْجَدِيَّة الْعَرَبِيَّة" ,"русский","user name spatiu", "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",""};
	public static String[] mail= {"@","@yahoo.com","@gmail.com","@info.uaic.ro","@русский","@الْعَرَبِيَّة","@",".com","ro"};
	public static String[] password= {"русский","الْعَرَبِيَّة","1","/"," ","","RmSwO1_?","AFS","","aaaaaaip"};
	public static void main(String[] args) throws InterruptedException
	{
		
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Tudor\\Desktop\\selenium\\chromedriver.exe");
		
		WebDriver driver=new ChromeDriver();
		
		
		driver.get("http://127.0.0.1:8000/users/signup/");
		for(String obj1:username)
			for(String obj2:mail)
				for(String obj3:password)
				{
					driver.findElement(By.name("email")).sendKeys(obj1+obj2);
					driver.findElement(By.name("password1")).sendKeys(obj2);
					driver.findElement(By.name("password2")).sendKeys(obj2);
					driver.findElement(By.name("first_name")).sendKeys(obj2);
					driver.findElement(By.name("last_name")).sendKeys(obj2);
					driver.findElement(By.xpath("//div[@class='bottom']")).click();
					Thread.sleep(1000);	
					driver.findElement(By.name("email")).clear();
					driver.findElement(By.name("password1")).clear();
					driver.findElement(By.name("password2")).clear();
					driver.findElement(By.name("first_name")).clear();
					driver.findElement(By.name("last_name")).clear();
				}
		driver.close();
		driver.quit();
			

	}

}
