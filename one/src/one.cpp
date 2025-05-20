#include "libone/one.h"

namespace libone {

long find(double (*f)(long), double y, long a, long b) {
    long low{a};
    long high{b};
    long middle{0};
    double f_middle{0.0};

    if ((a < 0) || (b < 0) || (a > b)){
        // check a and b to be non-negative and a < b
        return -1;
    }

    // binary search
    // split range in 2 halves and find in which part 'y' is located
    // low == high ensures the corner case where a == b 
    while(low <= high) {
        // calculate middle integer value of the current range
        middle = low + ((high - low) / 2);
        // evaluate integer into double
        f_middle = f(middle);
        if (f_middle == y) {
            // evaluated double matches 'y'
            return middle;
        } else if (f_middle < y) {
            // 'y' is in the upper half of the range, redefine low
            // + 1 ensures progress when the middle decimal gets truncated
            low = middle + 1;
        } else {
            // 'y' is in the lower half of the range, redefine high
            // - 1 ensures progress when the middle decimal gets truncated
            high = middle - 1;
        }
    }
        // when value not found
    return -1;
}

// Increasing function
static double square(long x) {
    return static_cast<double>(x * x);
}

long find_square(double y, long a, long b) {
    return find(square, y, a, b);
}

} // namespace libone