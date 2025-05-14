package tudelft.sum;

import java.util.ArrayList;
import java.util.Collections;

// Source: https://leetcode.com/problems/add-two-numbers/description/


class TwoNumbersSum {

    public ArrayList<Integer> addTwoNumbers(ArrayList<Integer> first, ArrayList<Integer> second) {
        ArrayList<Integer> f = new ArrayList<>(first);
        ArrayList<Integer> s = new ArrayList<>(second);

        Collections.reverse(f);
        Collections.reverse(s);

        int complement = 0;
        ArrayList<Integer> result = new ArrayList<>();

        for(int i = 0; i < Math.max(f.size(), s.size()); i++){
            int firstVal = i < f.size() ? f.get(i) : 0;
            int secondVal = i < s.size() ? s.get(i) : 0;
            int total = firstVal + secondVal + complement;

            complement = total / 10;
            result.add(i, total % 10);
        }

        if (complement > 0) {
            result.add(complement);
        }

        Collections.reverse(result);
        return result;
    }
}
