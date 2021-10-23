public int scheduleCourse(int[][] courses) {
    Arrays.sort(courses, (a, b) -> a[1] - b[1]);
    int dayCount = 0;
    int courseCount = 0;
    PriorityQueue<Integer> pq =new PriorityQueue<>((x, y) -> Integer.compare(y, x));
    for(int i = 0;i < courses.length; ++i){
        
        if(courses[i][1] >= dayCount + courses[i][0]){
            dayCount += courses[i][0];
            courseCount += 1;
            pq.add(courses[i][0]);
        }
        else{
            if(pq.size() > 0 && pq.peek() > courses[i][0]){
                dayCount += courses[i][0] - pq.poll();
                pq.add(courses[i][0]);
            }
        }
    }
    
    return courseCount;
}