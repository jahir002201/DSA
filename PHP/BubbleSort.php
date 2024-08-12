<?php
function bubbleSort(array $arr): array {
    $n = count($arr);
    
    for($i = 0; $i < $n - 1; $i++) {
        // Track if any swaps were made during this pass
        $swapped = false;
        
        for($j = 0; $j < $n - 1 - $i; $j++) {
            // If the current element is greater than the next, swap them
            if($arr[$j] > $arr[$j + 1]) {
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
            }
        }
        
        // If no swaps were made, the array is already sorted
        if(!$swapped) {
            break;
        }
    }
    
    return $arr;
}

// Example usage
$array = [33, 10, 59, 27, 2, 18, 40];
$sortedArray = bubbleSort($array);

print_r($sortedArray);
?>