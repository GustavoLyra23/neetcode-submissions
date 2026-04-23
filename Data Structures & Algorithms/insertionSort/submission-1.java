public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> newList = new ArrayList<>();
        if(pairs == null ||  pairs.isEmpty()){
            return newList;
        }
        newList.add(new ArrayList<>(pairs));

        int length = pairs.size();
        for (int i = 1; i < length; i++) {
            Pair current = pairs.get(i);
            int j = i - 1;
            while (j >= 0 && pairs.get(j).key > current.key) {
                pairs.set(j + 1, pairs.get(j));
                j--;
            }
            pairs.set(j + 1, current);
            newList.add(new ArrayList<>(pairs));
        }
        return newList;
    }
}