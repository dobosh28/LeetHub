/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length;
    let answer = new Array(n);
    let left = new Array(n);
    let right = new Array(n);

    left[0] = 1;
    for (let i = 1; i < n; i++) {
        left[i] = nums[i - 1] * left[i - 1];
    }

    right[n - 1] = 1;
    for (let i = n - 2; i >= 0; i--) {
        right[i] = nums[i + 1] * right[i + 1];
    }

    for (let i = 0; i < n; i++) {
        answer[i] = left[i] * right[i];
    }

    return answer;
};