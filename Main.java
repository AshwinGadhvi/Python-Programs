import java.util.*;
import java.util.List;
import java.util.stream.Collectors;
public class practice_set {
        
    /**
     * Creates a new instance of <code>practice_set</code>.
     */
    public main() {
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        List<Integer> op = Arrays.asList(10,20,30,40,50,60);
        List<Integer> ans = op.stream().sorted().collect(Collectors.toList());
        System.out.println(ans);
    }
}
