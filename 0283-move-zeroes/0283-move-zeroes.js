/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let n = nums.length;
    if (n < 2) return;
    
    let l = 0, r = 1;
    
    while (r < n) {
        if (nums[l] !== 0) {
            l++;
            r++;
        } else if(nums[r] === 0) {
            r++;
        } else {
            temp = nums[r];
            nums[r] = nums[l];
            nums[l] = temp;
        }
    }
};