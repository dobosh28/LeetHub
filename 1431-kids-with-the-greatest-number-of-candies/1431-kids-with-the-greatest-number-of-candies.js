/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let result = [];
    let maximum = candies[0];

    for (let i = 0; i < candies.length; i++) {
        if (candies[i] > maximum) {
            maximum = candies[i];
        }
    }

    for (let i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= maximum) {
            result.push(true);
        } else {
            result.push(false);
        }
    }
    

    return result;
};