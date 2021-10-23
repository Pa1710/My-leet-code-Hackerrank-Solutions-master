public class mySolution {
    public int maxArea(int[] height) {
        if (height.length < 2)
            return 0;
        int i = 0;
        int j = height.length - 1;
        int biggestContainer = 0;
        while (j > i) {
            int minH = Math.min(height[i], height[j]);
            int thisContainer = minH * (j - i);
            // System.out.println(i + " " + j);
            if (thisContainer > biggestContainer) {
                biggestContainer = thisContainer;
            }
            while (j > i && minH >= height[j]) {
                j--;
            }
            while (j > i && height[i] <= minH) {
                i++;
            }
        }
        return biggestContainer;
    }
}