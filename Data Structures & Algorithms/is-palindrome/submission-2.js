class Solution {
    isPalindrome(s) {
        let l = 0, r = s.length - 1;

        const isAlphaNum = (c) =>
            (c >= 'a' && c <= 'z') ||
            (c >= 'A' && c <= 'Z') ||
            (c >= '0' && c <= '9');

        while (l < r) {
            while (l < r && !isAlphaNum(s[l])) l++;
            while (l < r && !isAlphaNum(s[r])) r--;

            if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;

            l++;
            r--;
        }
        return true;
    }
}
