import java.util.HashMap;
import java.util.Map.Entry;


class Solution {
    public int numRabbits(int[] answers) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        int ans = 0;
        for (Integer key : answers) {
            if (hash.containsKey(key)) {
                hash.put(key, 1);
            } else {
                hash.put(key, hash.get(key) + 1);
            }
        }
        for (Entry<Integer, Integer> entry : hash.entrySet()) {
            if (entry.getValue() <= entry.getKey() + 1) {
                ans += entry.getKey() + 1;
            } else {
                ans += Math.ceil((double) entry.getValue() / (double) (entry.getKey() + 1)) * (entry.getKey() + 1);
            }
        }

        return ans;
    }
}