import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Student implements Comparable<Student> {
    private String imie;
    private String nazwisko;
    private ArrayList<Float> oceny;


    public Student(String imie, String nazwisko) {
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.oceny = new ArrayList<>();
    }

    public String getImie() {
        return imie;
    }

    public void setImie(String imie) {
        this.imie = imie;
    }

    public String getNazwisko() {
        return nazwisko;
    }

    public void setNazwisko(String nazwisko) {
        this.nazwisko = nazwisko;
    }

    public ArrayList<Float> getOceny() {
        return oceny;
    }

    public void setOceny(ArrayList<Float> oceny) {
        this.oceny = oceny;
    }

    public void addOcena(float ocena) {
        this.oceny.add(ocena);
    }

    public static float getMean(Student student){ //oczywiście może być niestatyczna "na this"
        if (student.getOceny().size() == 0)
            return 0;
        float s=0;
        for(float st : student.getOceny())
            s+=st;
        return (s/student.getOceny().size());
    }

    @Override
    public int compareTo(Student s1) {
        if ((this.nazwisko).compareTo(s1.getNazwisko()) == 1) {
            return 1;
        }

        if (this.nazwisko.equals(s1.getNazwisko()))
            if(this.imie.equals(s1.getImie()))
                if (getMean(this)==getMean(s1) ){
                    return 0;
                }
            else{ // to oczywiście do poprawy
                return 1;
                }

        return -1;
    }

    @Override
    public String toString() {
        return this.imie+ " "+ this.nazwisko+": "+getMean(this);
    }
}
