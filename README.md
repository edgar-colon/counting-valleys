# Counting Valleys

## Description

**The algorithm proceeds through the following steps to count the valleys crossed by the hiker:**

**Creation of the Elevation Changes Array:** The process begins by creating an array called elevation_changes, which represents the changes in altitude as the hiker progresses along the path. This array starts with a value of 0, representing sea level.

**Traversal of the Array:** Next, the elevation_changes array is traversed as the hiker progresses along the path. For each step on the path, the array is updated with the corresponding change in altitude. For example, if the hiker takes a step upwards (represented by 'U'), the altitude is incremented by 1. If they take a step downwards (represented by 'D'), the altitude is decremented by 1.

**Identification of Valley Patterns:** Once the elevation changes array has been created, patterns representing the entrance and exit of a valley are identified. A valley is defined as a sequence of steps downwards followed by a step upwards. Therefore, the entrance and exit patterns of a valley are [0, -1] and [-1, 0] respectively.

**Counting Crossed Valleys:** Finally, the number of times an entrance pattern followed by an exit pattern is found in the elevation changes array is counted. Each time this pattern is found, the counter of crossed valleys is incremented.

**Result:** The final result is the total number of valleys crossed by the hiker during the hike.

## Installation

To install the program dependencies, ensure you have Python and pip installed on your system. Then, run the following command in your terminal:

```
pip install -r requirements.txt
```

## Running the Tests

To run the unit tests, simply execute the `tests.py` file. You can do this by running the following command in your terminal:

```
python tests.py
```