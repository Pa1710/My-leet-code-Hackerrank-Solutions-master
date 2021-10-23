public class mySolution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> ladderLog = new PriorityQueue<>();
        int totalLadders = ladders;
        int i = 0;
        while (i < heights.length - 1) {
            if (heights[i] >= heights[i + 1]) {
                i++;
                continue;
            } else {
                int heightDiff = heights[i + 1] - heights[i];
                if (ladders > 0) {
                    ladders--;
                    ladderLog.add(heightDiff);
                    i++;
                    continue;
                }
                if (totalLadders > 0 && heightDiff > ladderLog.peek()) {
                    if (bricks >= ladderLog.peek()) {
                        ladderLog.add(heightDiff);
                        bricks -= ladderLog.poll();
                        i++;
                        continue;
                    } else {
                        return i;
                    }
                }
                if (totalLadders > 0 && heightDiff < ladderLog.peek() && bricks >= heightDiff) {
                    bricks -= heightDiff;
                    i++;
                    continue;
                }
                if (bricks < heightDiff) {
                    return i;
                }
                if (bricks >= heightDiff) {
                    bricks -= heightDiff;
                    i++;
                }
            }
        }
        return i;
    }
}
