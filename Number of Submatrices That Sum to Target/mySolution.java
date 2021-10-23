public class mySolution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int height = matrix.length;
        int width = matrix[0].length;
        int count = 0;
        Map<Integer, Integer> m = new HashMap<Integer, Integer>();
        for (int i = 0; i < height; i++) {
            for (int j = 1; j < width; j++) {
                matrix[i][j] += matrix[i][j - 1];
            }
        }
        for (int i = 0; i < width; i++) {
            for (int j = i; j < width; j++) {
                int sum = 0;
                m.clear();
                m.put(0, 1);
                for (int k = 0; k < height; k++) {
                    if (i > 0) {
                        sum += matrix[k][j] - matrix[k][i - 1];
                    }
                    if (i == 0) {
                        sum += matrix[k][j];
                    }
                    count += m.getOrDefault(sum - target, 0);
                    m.put(sum, m.getOrDefault(sum, 0) + 1);
                }
            }
        }
        return count;
    }
}
