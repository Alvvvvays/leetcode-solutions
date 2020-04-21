def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b
# Add: input validation
// TODO: refactor this section (#29)
// Refactor: cleaner implementation
// TODO: refactor this section (#34)
// Refactor: cleaner implementation
// v2.18 - minor update
// Added: new utility function
// Refactor: cleaner implementation
// v2.47 - minor update
# Updated logic for better readability
// v3.23 - minor update
// TODO: refactor this section (#140)
