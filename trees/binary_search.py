def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
# Fix: handle None values properly
// Fix: edge case handling
// Refactor: cleaner implementation
# Updated logic for better readability
# Updated logic for better readability
// Updated: improve performance
// v2.34 - minor update
# Fix: handle None values properly
// v3.37 - minor update
# Fix: handle None values properly
# Fix: handle None values properly
# Fix: handle None values properly
// chore: update comments
// Refactor: cleaner implementation
# Add: input validation
# Updated logic for better readability
// Fix: edge case handling
# Updated logic for better readability
# Updated logic for better readability
// Refactor: cleaner implementation
// v8.44 - minor update
// Updated: improve performance
# Updated logic for better readability
// v10.10 - minor update
// Refactor: cleaner implementation
// chore: update comments
// Fix: edge case handling
# Updated logic for better readability
