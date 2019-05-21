import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class News 
{
	public static void main(String[] args)
	{
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Tudor\\Desktop\\selenium\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		driver.get("http://fiistudent.ddns.us/news/");
		
		List<WebElement> list=new ArrayList<>();
		list=driver.findElements(By.xpath("//p[@class='top']/a"));
		for(WebElement obj:list)
			System.out.println(obj.getText());

		
		try 
		{
		for(WebElement obj:list)
		{
			obj.click();
			driver.navigate().back();
		}
		}catch(Exception e)
		{
			System.out.println(e.getMessage());
		}

	}
}
