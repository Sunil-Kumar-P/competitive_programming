// 7. Reverse Integer

// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

// Example 1:

// Input: x = 123
// Output: 321

// Example 2:

// Input: x = -123
// Output: -321

// Example 3:

// Input: x = 120
// Output: 21

class reverseInteger {
    public int reverse(int x) {
        boolean negative = false;
        if (x < 0) {
            negative = true;
            x = Math.abs(x);
        }
        long result = 0;
        while (x > 0) {
            int digit = x % 10;
            result = result * 10 + digit;
            x /= 10;
        }
        if (negative) {
            result *= -1;
        }
        if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
            return 0;
        }
        return (int) result;
    }
    public static void main(String[] args) {
        int x = -123;
        reverseInteger val = new reverseInteger();
        System.out.println(val.reverse((x)));
    }
}