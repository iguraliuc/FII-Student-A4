import java.util.Set;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import okhttp3.Cookie;

public class Cookies 
{
	public static void main(String[] args) throws InterruptedException
	{
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Tudor\\Desktop\\selenium\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		driver.get("http://127.0.0.1:8000/users/login/");
		
		driver.findElement(By.name("username")).sendKeys("tudor.manoleasa@info.uaic.ro");
		driver.findElement(By.name("password")).sendKeys("aaaaaaip");
		driver.findElement(By.xpath("//input[@type='submit']")).click();
		Set<org.openqa.selenium.Cookie> set=driver.manage().getCookies();
		Thread.sleep(3000);
		
		System.out.println(set.size());
		for(org.openqa.selenium.Cookie cookie:set)
		{
			System.out.println(cookie.getName());
		}
		
		driver.manage().deleteCookieNamed("sessionid");
		
		driver.findElement(By.xpath("//a[@href='/news/']")).click();
		
		Thread.sleep(2000);
		
		System.out.println(driver.manage().getCookies().size());
		driver.close();
		driver.quit();
	}
}
