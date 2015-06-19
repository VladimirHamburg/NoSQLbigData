package app.gui;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;
import java.util.HashSet;
import java.util.Set;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import com.mongodb.MongoClient;
import com.mongodb.util.Hash;

import app.db.DBHbase;
import app.db.DBMongo;
import app.db.DBRedis;
import app.entities.Data;
import app.entities.Timer;

public class MainFrame extends JFrame {
	private static Timer timer = new Timer();

	private JLabel lDatenbank = new JLabel("Datenbank ");
	private JRadioButton radioButtonRedis;
	private JRadioButton radioButtonMongo;
	private JRadioButton radioButtonHBase;

	private JLabel lSucheNach = new JLabel("Suche nach ");
	private JRadioButton radioButtonPlz;
	private JRadioButton radioButtonCity;
	private JTextField tfSearch = new JTextField("", 20);
	private JButton bSearch = new JButton("Search...");

	private JPanel pNorth = new JPanel(new BorderLayout());
	private JPanel pNorthCenter = new JPanel(new FlowLayout());
	private JPanel pNorthNorth = new JPanel(new FlowLayout());

	private JPanel pNorthSouth = new JPanel(new FlowLayout());
	private JPanel pSouth = new JPanel(new FlowLayout());

	private JTextArea textArea;

	private DBRedis dbRedis = new DBRedis("localhost", 6379);
	private DBMongo dbMongo = new DBMongo("localhost", 27017);
	private DBHbase dbHbase = new DBHbase("localhost");

	private final int ANZAHL_DURCHLAUFE = 1;

	public MainFrame() {
		super("NoSQL");
		this.setSize(600, 300);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLayout(new BorderLayout());
		init();
		this.setVisible(true);
	}

	private void init() {
		ButtonGroup groupDb = new ButtonGroup();
		radioButtonRedis = new JRadioButton("Redis");
		radioButtonRedis.setSelected(true);
		radioButtonMongo = new JRadioButton("Mongo");
		radioButtonHBase = new JRadioButton("HBase"); 
		groupDb.add(radioButtonRedis);
		groupDb.add(radioButtonMongo);
		groupDb.add(radioButtonHBase); 

		ButtonGroup groupSearch = new ButtonGroup();
		radioButtonPlz = new JRadioButton("PLZ");
		radioButtonPlz.setSelected(true);
		radioButtonCity = new JRadioButton("City");
		groupSearch.add(radioButtonPlz);
		groupSearch.add(radioButtonCity);

		bSearch.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				timer.start("db zugriff");
				for (int i = 0; i < ANZAHL_DURCHLAUFE; i++) {
					if (radioButtonPlz.isSelected()) {

						Data result = null;
						if (radioButtonHBase.isSelected()){
							result = dbHbase.getDataByPLZ(tfSearch.getText());
							textArea.append("> HBase \n");			
						}
						if (radioButtonRedis.isSelected()){
							result = dbRedis.getDataByPLZ(tfSearch.getText());
							textArea.append("> Redis \n");
						}
						if (radioButtonMongo.isSelected()){
							result = dbMongo.getDataByPLZ(tfSearch.getText());
							textArea.append("> MongoDB \n");
						}
						if (result == null)
							textArea.append("> 0 rows \n");
						else {
							textArea.append("> CITY= " + result.getCity() + "\n");
							textArea.append("> STATE= " + result.getState() + "\n");
							
						}

					} else {
						Set<String> result = new HashSet<String>();
						if (radioButtonHBase.isSelected()){
							result = DBHbase.getPLZByCity(tfSearch.getText().toUpperCase());
							textArea.append("> HBase \n");
						}
						if (radioButtonRedis.isSelected()){
							result = dbRedis.getPLZByCity(tfSearch.getText().toUpperCase());
							textArea.append("> Redis \n");
						}
						if (radioButtonMongo.isSelected()){
							result = dbMongo.getPLZByCity(tfSearch.getText().toUpperCase());
							textArea.append("> MognoDB \n");
						}
						textArea.append(">" + "PLZ zu " + tfSearch.getText() + ": "
								+ result + "\n");
					}
				}

				long timeSelect = timer.stop("db zugriff");
				textArea.append("Dauer : " + timeSelect / ANZAHL_DURCHLAUFE + " ms - "
						+ (timeSelect / ANZAHL_DURCHLAUFE) / 60000 + "m"
						+ (((timeSelect / ANZAHL_DURCHLAUFE) / 1000) % 60) + "s\n");
			}
		});

		pNorthCenter.add(lSucheNach);
		pNorthCenter.add(radioButtonPlz);
		pNorthCenter.add(radioButtonCity);

		pNorthNorth.add(lDatenbank);
		pNorthNorth.add(radioButtonRedis);
		pNorthNorth.add(radioButtonMongo);
		pNorthNorth.add(radioButtonHBase); 

		pNorthSouth.add(tfSearch);
		pNorthSouth.add(bSearch);

		textArea = new JTextArea(5, 20);
		JScrollPane scrollPane = new JScrollPane(textArea);
		scrollPane.setAutoscrolls(true);
		textArea.setEditable(false);

		pNorth.add(pNorthNorth, BorderLayout.NORTH);
		pNorth.add(pNorthCenter, BorderLayout.CENTER);
		pNorth.add(pNorthSouth, BorderLayout.SOUTH);
		this.add(pNorth, BorderLayout.NORTH);
		this.add(scrollPane, BorderLayout.CENTER);
		this.add(pSouth, BorderLayout.SOUTH);

	}

	public static void main(String[] args) {
		MainFrame mf = new MainFrame();
	}

}
