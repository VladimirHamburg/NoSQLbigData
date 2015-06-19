package app.entities;

import java.util.ArrayList;
import java.util.List;

import redis.clients.jedis.Jedis;

public class Data {

	private String plz;
	private String city;
	private float[] loc;
	private int pop;
	private String state;
	
	public Data(String plz, String city, float[] loc, int pop, String state) {
		this.plz = plz;
		this.city = city;
		this.loc = loc;
		this.pop = pop;
		this.state = state;
	}

	public String getPlz() {
		return plz;
	}

	public void setPlz(String plz) {
		this.plz = plz;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public float[] getLoc() {
		return loc;
	}

	public void setLoc(float[] loc) {
		this.loc = loc;
	}

	public int getPop() {
		return pop;
	}

	public void setPop(int pop) {
		this.pop = pop;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}
	
	public List<List<Object>> getAll(){
		List<List<Object>> res = new ArrayList<>();
		
		
		
		return res;
	}
	
}
