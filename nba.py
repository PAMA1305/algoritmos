def points_per_48(ppg, mpg):
    if mpg == 0:
        return 0
    # Calculate extrapolated points for 48 minutes
    extrapolated_ppg = (ppg / mpg) * 48
    # Round to the nearest tenth
    return round(extrapolated_ppg, 1)

# Example usage:
print(points_per_48(12, 20))  # Output: 28.8
print(points_per_48(10, 10))  # Output: 48.0
print(points_per_48(5, 17))   # Output: 14.1
print(points_per_48(0, 0))    # Output: 0