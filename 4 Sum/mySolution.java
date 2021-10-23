class mySolution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length - 1; ++i) {
            if (i > 0) {
                if (nums[i - 1] == nums[i]) {
                    continue;
                }
            }
            for (int j = i + 1; j < nums.length; ++j) {

                if (nums[j - 1] == nums[j] && j != i + 1) {
                    continue;
                }
                int sum1 = nums[i] + nums[j];
                int k = j + 1;
                int m = nums.length - 1;
                while (k < m) {
                    int sum = sum1 + nums[k] + nums[m];
                    if (sum < target) {
                        k++;
                        while (nums[k - 1] == nums[k] && k < m) {
                            k++;
                        }
                        continue;
                    }
                    if (sum > target) {
                        m--;
                        while (nums[m + 1] == nums[m] && m > k) {
                            m--;
                        }
                        continue;
                    }
                    if (sum == target) {
                        List<Integer> l = new ArrayList<Integer>(4);
                        l.add(nums[i]);
                        l.add(nums[j]);
                        l.add(nums[k]);
                        l.add(nums[m]);

                        ans.add(l);

                        k++;
                        while (nums[k - 1] == nums[k] && k < m) {
                            k++;
                        }
                        m--;
                        while (nums[m + 1] == nums[m] && m > k) {
                            m--;
                        }
                        continue;
                    }
                }
            }
        }
        return ans;
    }
}