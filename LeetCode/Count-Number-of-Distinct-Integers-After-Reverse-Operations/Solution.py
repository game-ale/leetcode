    HashSet<Integer> set = new HashSet<Integer>();

    for(int i=0; i<nums.length; i++) {
        //if(!set.contains(nums[i])) {
            set.add(nums[i]);
            set.add(reverseDigits(nums[i]));
        //}
    }

    return set.size();
}

public int reverseDigits(int num) {

    int n = 0;
    while(num > 0) {
        n *= 10;
        n += num % 10;
        num /= 10;
    }
    return n;
}