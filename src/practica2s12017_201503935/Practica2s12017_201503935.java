/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2s12017_201503935;

import javax.swing.UIManager;
import de.javasoft.plaf.synthetica.SyntheticaOrangeMetallicLookAndFeel;

/**
 *
 * @author ddani
 */
public class Practica2s12017_201503935 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            UIManager.setLookAndFeel(new SyntheticaOrangeMetallicLookAndFeel());
        }catch(Exception ex){
            
        }
        Primera pr = new Primera();
        pr.setVisible(true);
    }
    
}
