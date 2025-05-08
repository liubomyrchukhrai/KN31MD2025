#include "calculator.h"
#include <iostream>
#include <cassert>

int main() {
    Calculator calc;

    // Addition
    assert(calc.add(3, 4) == 7);
    assert(calc.add(-1, -2) == -3);

    // Subtraction
    assert(calc.subtract(10, 5) == 5);
    assert(calc.subtract(0, 5) == -5);

    // Multiplication
    assert(calc.multiply(3, 4) == 12);
    assert(calc.multiply(0, 100) == 0);

    // Division
    assert(calc.divide(10, 2) == 5.0);
    assert(calc.divide(7, 2) == 3.5);

    // Division by zero (should throw)
    try {
        calc.divide(1, 0);
        std::cerr << "Division by zero test failed!\n";
        return 1;
    } catch (const std::invalid_argument& e) {
        std::cout << "Division by zero correctly threw exception.\n";
    }

    std::cout << "All tests passed!\n";
    return 0;
}
