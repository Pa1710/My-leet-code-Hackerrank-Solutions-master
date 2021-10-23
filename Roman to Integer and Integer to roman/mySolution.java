import java.util.HashMap;

public class RomanNumerals {

    public static String toRoman(int n) {
        String s = "";
        if (n >= 1000) {
            int x = n / 1000;
            while (x > 0) {
                s += "M";
                n -= 1000;
                x--;
            }
        }
        if (n >= 500) {
            if (n >= 900) {
                n -= 900;
                s += "CM";
            } else {
                n -= 500;
                s += "D";
            }
        }
        if (n >= 100) {
            if (n >= 400) {
                n -= 400;
                s += "CD";
            }
            int y = n / 100;
            while (y > 0) {
                n -= 100;
                s += "C";
                y--;
            }
        }
        if (n >= 50) {
            if (n >= 90) {
                n -= 90;
                s += "XC";
            } else {
                n -= 50;
                s += "L";
            }
        }
        if (n >= 10) {
            if (n >= 40) {
                n -= 40;
                s += "XL";
            }
            while (n >= 10) {
                s += "X";
                n -= 10;
            }
        }

        if (n >= 5) {
            if (n == 9) {
                n -= 9;
                s += "IX";
            } else {
                n -= 5;
                s += "V";
            }
        }
        if (n > 0) {
            if (n == 4) {
                n -= 4;
                s += "IV";
            }
            while (n > 0) {
                n -= 1;
                s += "I";
            }
        }

        return s;
    }

    public static int fromRoman(String romanNumeral) {
        HashMap<Character, Integer> m = new HashMap<Character, Integer>();
        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);
        int sum = 0;
        if (romanNumeral.length() == 0) {
            return m.get(romanNumeral.charAt(0));
        }
        for (int i = 0; i < romanNumeral.length() - 1; ++i) {
            if (m.get(romanNumeral.charAt(i)) < m.get(romanNumeral.charAt(i + 1))) {
                sum -= m.get(romanNumeral.charAt(i));
                continue;
            }
            sum += m.get(romanNumeral.charAt(i));
        }
        sum += m.get(romanNumeral.charAt(romanNumeral.length() - 1));
        return sum;
    }
}