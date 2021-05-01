/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        HashMap<Integer, Employee> importance = new HashMap<Integer, Employee>();
        Employee target = null;
        for (Employee obj: employees) {
            importance.put(obj.id, obj);
            if (obj.id == id) {
                target = obj;
            }
        }
        int ans = target.importance;
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int subId : target.subordinates) {
            queue.offer(subId);
        }
        while (!queue.isEmpty()) {
            Queue<Integer> queue_ = new LinkedList<Integer>();
            while (!queue.isEmpty()) {
                Employee obj = importance.get(queue.poll());
                ans += obj.importance;
                for (int subId : obj.subordinates) {
                    queue_.offer(subId);
                }
            }
            queue = queue_;
        }

        return ans;
    }
}