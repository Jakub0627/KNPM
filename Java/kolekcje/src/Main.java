import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        // generic tam gdzie możemy dostawiać typy <...>
        LinkedList<String> grupa = new LinkedList<>();// zobacz gdzie String
        grupa.add("Kowalski");
        grupa.add("Nowak");
        grupa.add("Adamowski");
        Collections.sort(grupa);
        for (String x: grupa){
            System.out.println(x);
        }
        Student s1 = new Student("Adam", "Adamski");
        s1.addOcena(5);
        s1.addOcena(3);

        Student s2 = new Student("Adam", "Adamski");
        s2.addOcena(4);
        s2.addOcena(4);

        Student s3 = new Student("Adam", "Abba");
        s3.addOcena(5);
        s3.addOcena(4);

        LinkedList<Student> grupaFull = new LinkedList<>();
        grupaFull.add(s1);
        grupaFull.add(s2);
        grupaFull.add(s3);
        Collections.sort(grupaFull);
        System.out.println(grupaFull);

    }
}