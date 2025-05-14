package tudelft.sum;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class TwoNumbersSumTest {
    private TwoNumbersSum sum = new TwoNumbersSum();
    private ArrayList<Integer> list(Integer... digits) {
        return new ArrayList<>(Arrays.asList(digits));
    }

    // Caso: suma sin acarreo
    @Test
    public void sumWithoutCarry() {
        // 12 + 23 = 35
        // [1,2] + [2,3] = [3,5]
        assertEquals(list(3, 5), sum.addTwoNumbers(list(1, 2), list(2, 3)));
    }

    // Caso con acarreo en la última posición
    @Test
    public void sumWithFinalCarry() {
        // 99 + 1 = 100
        // [9,9] + [1] = [1,0,0]
        assertEquals(list(1, 0, 0), sum.addTwoNumbers(list(9, 9), list(1)));
    }

    // Caso con listas de distinto tamaño
    @Test
    public void sumWithDifferentSizes() {
        // 100 + 23 = 123
        // [1,0,0] + [2,3] = [1,2,3]
        assertEquals(list(1, 2, 3), sum.addTwoNumbers(list(1, 0, 0), list(2, 3)));
    }

    // Caso especial: suma de ceros
    @Test
    public void sumOfZeros() {
        // 0 + 0 = 0 -> [0] + [0] = [0]
        assertEquals(list(0), sum.addTwoNumbers(list(0), list(0)));
    }

    // Caso con acarreo interno
    @Test
    public void sumWithCarryInMiddle() {
        // 56 + 67 = 123
        // [5,6] + [6,7] = [1,2,3]
        assertEquals(list(1, 2, 3), sum.addTwoNumbers(list(5, 6), list(6, 7)));
    }

    // Caso mínimo con acarreo (5 + 5 = 10)
    @Test
    public void singleDigitCarry() {
        // 5 + 5 = 10
        // [5] + [5] = [1,0]
        assertEquals(list(1, 0), sum.addTwoNumbers(list(5), list(5)));
    }
}
