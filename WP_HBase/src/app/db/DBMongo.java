package app.db;

import app.entities.Data;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.MongoClient;

import java.net.UnknownHostException;
import java.util.HashSet;
import java.util.Set;

public class DBMongo {
	private DBCollection coll;

	public DBMongo(String host, int port) {
		try {
			MongoClient mongoClient = new MongoClient(host, port);
			DB db = mongoClient.getDB("plz");
			coll = db.getCollection("plzs");
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}
	}

	public Data getDataByPLZ(String key) {
		DBObject myDoc = coll.findOne(new BasicDBObject("_id", key));
		if (myDoc == null)
			return null; 
		return new Data(myDoc.get("_id") + "", myDoc.get("city") + "", null, Integer.parseInt(myDoc.get("pop") + ""),
				myDoc.get("state") + "");
	}

	public Set<String> getPLZByCity(String city) {
		DBCursor cursor = coll.find(new BasicDBObject("city", city));
		Set<String> res = new HashSet<String>();
		try {
			while (cursor.hasNext()) {
				res.add(cursor.next().get("_id") + "");
			}
		} finally {
			cursor.close();
		}
		return res;
	}
}
