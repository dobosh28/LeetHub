/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let result = '';
    let i = 0;
    const n = s.length;
    
    while (i < n) {
        while ( i < n && s[i] === ' ') i++;
        if (i >= n) break;
        let j = i + 1;
        while ( j < n && s[j] !== ' ') j++;
        const sub = s.substring(i, j);
        result = result.length === 0 ? sub : sub + ' ' + result;
        i = j + 1;
    }
    return result;
};