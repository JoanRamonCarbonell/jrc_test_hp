#pragma once

namespace libone {

/**
 * @brief Increasing method to return the square of a value.
 * @param y arbitrary double-float value
 * @param a range low value
 * @param b range high value
 * @return double square of input. 
 */
long find_square(double y, long a, long b);

/**
 * @brief Method to find a value within a range, that being evaluated with another provided function, matches an arbitrary value.
 * @param f increasing function. Receives an integer to evaluate it to a float. 
 * @param y arbitrary double-float value
 * @param a range low value
 * @param b range high value
 * @return long value contained in the range, if its evaluation matches the arbitrary double. 
 *         Returns -1 otherwise. 
 */
long find(double (*f)(long), double y, long a, long b);

} // namespace libone