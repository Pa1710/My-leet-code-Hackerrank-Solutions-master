/**
 * mySolution
 */
public class mySolution {

    public int leastBricks(List<List<Integer>> wall) {
        Map<Integer, Integer> m = new HashMap<>();
        int max = 0;
        for (int i = 0; i < wall.size(); ++i) {
            int sum = 0;
            for (int j = 0; j < wall.get(i).size() - 1; ++j) {
                sum += wall.get(i).get(j);
                m.put(sum, m.getOrDefault(sum, 0) + 1);
                if (m.get(sum) > max) {
                    max = m.get(sum);

                }
            }
        }
        // Set s = m.entrySet();
        // Iterator itr = s.iterator();
        // while(itr.hasNext()){
        // Map.Entry entry=(Map.Entry)itr.next();
        // int temp = (int) entry.getValue();
        // if(temp >= max){
        // secondMax = max;
        // max = temp;
        // }
        // }
        // if(max-secondMax == wall.size() && wall.get(0).size() > 1){return
        // max-secondMax - 1;}
        return wall.size() - max;
    }
}