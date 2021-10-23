public class mySolution {
    public int jump(int[] nums) {
        int cur = 0, bestJump = 0, count = 0, afterJump = 0;
        while (afterJump < nums.length - 1) {
            for (int i = cur; i <= afterJump; i++) {
                bestJump = Math.max(bestJump, i + nums[i]);
            }
            cur = afterJump + 1;
            afterJump = bestJump;
            count++;
        }
        return count;
    }
}
