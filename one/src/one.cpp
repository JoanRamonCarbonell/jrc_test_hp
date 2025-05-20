#include "libone/one.h"

namespace libone {

long find(double (*f)(long), double y, long a, long b) {
    long low{a};
    long high{b};
    long middle{0};
    double f_middle{0.0};

    if ((a < 0) || (b < 0)) {
        // check a and b to be non-negative
        return -1;
    }

    // binary search
    // split range in 2 halves and find in which part 'y' is located
    while(low < high) {
        // calculate middle integer value of the current range
        middle = low + ((high-low)/2);
        // evaluate integer into double
        f_middle = f(middle);
        if (f_middle == y) {
            // evaluated double matches 'y'
            return middle;
        } else if (f_middle < y) {
            // 'y' is in the upper half of the range, redefine low
            low = middle;
        } else {
            // 'y' is in the lower half of the range, redefine high
            high = middle;
        }
    }
        // when value not found
    return -1;
}

} // namespace libone