import java.awt.List;
import java.sql.Driver;
import java.util.ArrayList;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestLinks 
{
	public static String[] vector= {"Biblioteci", "Burse" , "Cantinele" , "Cazare", "Contact", "verifica", "Documente", "Ghidul", "academice", "Orientare", "Regulamente", "Reprezentarea", "Servicii"};
	public static void main(String[] args) throws InterruptedException
	{
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Tudor\\Desktop\\selenium\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		driver.get("http://127.0.0.1:8000/resources/");
		
		
		java.util.List<WebElement> list=new ArrayList<>();
		list=driver.findElements(By.xpath("//ul[@class='resources-list']/li/a"));
		for(WebElement obj:list)
			System.out.println(obj.getText());
		
		for(String elem:vector)
		{
			String xpath="//a[@href and contains(text(),\"" +elem+ "\")]";
			driver.findElement(By.xpath(xpath)).click();
			driver.navigate().back();
			Thread.sleep(1000);
		}									
		
		
		vector= new String[]{"Orar", "Boards", "Noutati", "Resurse"};
		
		for(String elem:vector)
		{
			String xpath="//a[@href and contains(text(),\"" +elem+ "\")]";
			driver.findElement(By.xpath(xpath)).click();
			driver.navigate().back();
			Thread.sleep(1000);
		}
		
		driver.close();
		driver.quit();
	}
}
