package app.db;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.KeyValue;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.filter.BinaryComparator;
import org.apache.hadoop.hbase.filter.CompareFilter;
import org.apache.hadoop.hbase.filter.FamilyFilter;
import org.apache.hadoop.hbase.filter.Filter;
import org.apache.hadoop.hbase.filter.FilterList;
import org.apache.hadoop.hbase.filter.QualifierFilter;
import org.apache.hadoop.hbase.filter.ValueFilter;
import org.apache.hadoop.hbase.util.Bytes;

import app.entities.Data;

public class DBHbase {

	public DBHbase(String host) {
	}

	public static Set<String> getPLZByCity(String city) {
		Set<String> resultPLZ = new HashSet<String>();

		List<Filter> filters = new ArrayList<Filter>();
		Filter famFilter = new FamilyFilter(CompareFilter.CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("data"))); 
		
		filters.add(famFilter); 
		
		Filter colFilter = new QualifierFilter(CompareFilter.CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes("city"))); 
		filters.add(colFilter); 
		 
		Filter valFilter = new ValueFilter(CompareFilter.CompareOp.EQUAL, new BinaryComparator(Bytes.toBytes(city)));
		
		
		filters.add(valFilter); 
		
		FilterList fl = new FilterList(FilterList.Operator.MUST_PASS_ALL, filters); 
		
		Scan scan = new Scan(); 
		scan.setFilter(fl); 
		String result = ""; 
		
		Configuration config = HBaseConfiguration.create();
		HTable table;
		try {
			table = new HTable(config, "plz");
			ResultScanner scanner = table.getScanner(scan); 
			
			for (Result res: scanner) {
				for (KeyValue kv : res.raw()) {
					byte [] plz = kv.getKey(); 
					resultPLZ.add(Bytes.toString(plz).substring(0,8));
				}
			}
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return resultPLZ;
	}

	public Data getDataByPLZ(String plz) {
		String city = "---";
		String state = "---";
		try {
			city = readValue(plz, "city");
			state = readValue(plz, "state");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return new Data(plz, city, null, 0, state);
	}

	public static String readValue(String k, String v) throws IOException {
		Configuration config = HBaseConfiguration.create();
		HTable table = new HTable(config, "plz");
		Get g = new Get(Bytes.toBytes(k));
		Result result = table.get(g);
		byte[] value = result.getValue(Bytes.toBytes("data"), Bytes.toBytes(v));
		return Bytes.toString(value);
	}

}
