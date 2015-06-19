import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.MasterNotRunningException;
import org.apache.hadoop.hbase.ZooKeeperConnectionException;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.util.Bytes;

public class HBaseConnection
{
 public static void main(String[] args) throws IOException
 {
	//String tabName = "DATAplz1";
	//createTable(tabName); 
	readValue("62045", "city");
	
 }
 
 
 public static void getPLZ(String k, String v) throws IOException{
	 Configuration config = HBaseConfiguration.create(); 
	 HTable table = new HTable(config, "plz");
	 Get g = new Get(Bytes.toBytes(k)); 
	 Result result = table.get(g); 
	 byte[] value = result.getValue(Bytes.toBytes("data"), Bytes.toBytes(v)); 
	 System.out.println(Bytes.toString(value));
 }
 
 public static void readValue(String k, String v) throws IOException{
	 Configuration config = HBaseConfiguration.create(); 
	 HTable table = new HTable(config, "plz");
	 Get g = new Get(Bytes.toBytes(k)); 
	 Result result = table.get(g); 
	 byte[] value = result.getValue(Bytes.toBytes("data"), Bytes.toBytes(v)); 
	 System.out.println(Bytes.toString(value));
 }
 
 
 
 
 
 
 
 public static void createTable(String tabName) throws MasterNotRunningException, ZooKeeperConnectionException, IOException{
	  HBaseConfiguration hc = new HBaseConfiguration(new Configuration());
	  HTableDescriptor ht = new HTableDescriptor(tabName); 
	  ht.addFamily( new HColumnDescriptor("Data"));
	  System.out.println( "connecting" );
	  HBaseAdmin hba = new HBaseAdmin( hc );
	  System.out.println( "Creating Table" );
	  hba.createTable( ht );
	  System.out.println("Done......");
 }
}