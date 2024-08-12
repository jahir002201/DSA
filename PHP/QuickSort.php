<?php
function quickSort(array $arr): array {
    // Base case: arrays with 0 or 1 element are already sorted
    if(count($arr) < 2) {
        return $arr;
    }
    
    // Choose the pivot (for simplicity, we'll take the first element)
    $pivot = $arr[0];
    
    // Partition the array into two halves
    $left = [];  // Elements less than the pivot
    $right = []; // Elements greater than the pivot
    
    for($i = 1; $i < count($arr); $i++) {
        if($arr[$i] <= $pivot) {
            $left[] = $arr[$i];
        } else {
            $right[] = $arr[$i];
        }
    }
    
    // Recursively sort the left and right halves and combine them with the pivot
    return array_merge(quickSort($left), [$pivot], quickSort($right));
}

// Example usage
$array = [33, 10, 59, 27, 2, 18, 40];
$sortedArray = quickSort($array);

print_r($sortedArray);
?>