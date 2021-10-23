public class mySolution {
    public int[] constructArray(int n, int k) {
        int[] l = new int[n];
        int j = k + 1;
        int i = 1;
        int ptr = 0;
        if (k == 1) {
            for (int kk = 0; kk < n; ++kk) {
                l[kk] = kk + 1;
            }
            return l;
        }
        while (ptr < k + 1) {
            if (ptr % 2 == 0) {
                l[ptr] = j;

                j -= 1;
                ptr += 1;
            } else {
                l[ptr] = i;

                i += 1;
                ptr += 1;
            }
        }
        int m = k + 1;
        while (m < n) {
            l[m] = m + 1;
            ++m;
        }
        return l;
    }
}
