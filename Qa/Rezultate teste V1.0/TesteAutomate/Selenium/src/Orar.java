
import java.awt.List;
import java.sql.Driver;
import java.util.ArrayList;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;



public class Orar 
{
	public static void main(String[] args) throws InterruptedException
	{
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\Tudor\\Desktop\\selenium\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		driver.get("http://127.0.0.1:8000/orar/");
		
		String firstXpath="//button[@type='submit']";
		
		java.util.List<WebElement> lista=new ArrayList<>();
		lista=driver.findElements(By.xpath(firstXpath));
		System.out.println(lista.get(0));
		
		
		for(int i=1;i<=30;i++)
		{
			Select category=new Select(driver.findElement(By.name("materie")));
			category.selectByIndex(i);
			for(int j=1;j<=2;j++)
			{
				Select category2=new Select(driver.findElement(By.name("grupa")));
				category2.selectByIndex(j);
				for(int k=1;k<=2;k++)
				{
					Select category3=new Select(driver.findElement(By.name("profesor")));
					category3.selectByIndex(k);
					for(int d=1;d<=2;d++)
					{
						Select category4=new Select(driver.findElement(By.name("sala")));
						category4.selectByIndex(d);
					}
				}
			}
		}
		
		
		driver.close();
		driver.quit();
		
	}
}
