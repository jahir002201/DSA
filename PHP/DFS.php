<?php
function dfs($graph, $start, &$visited = []) {
    $visited[] = $start; // Mark the node as visited

    // Recursively visit all adjacent vertices that have not been visited
    foreach ($graph[$start] as $neighbor) {
        if (!in_array($neighbor, $visited)) {
            dfs($graph, $neighbor, $visited);
        }
    }

    return $visited;
}

// Example graph represented as an adjacency list
$graph = [
    'A' => ['B', 'C'],
    'B' => ['A', 'D', 'E'],
    'C' => ['A', 'F', 'G'],
    'D' => ['B'],
    'E' => ['B', 'H'],
    'F' => ['C'],
    'G' => ['C'],
    'H' => ['E']
];

$result = dfs($graph, 'A');
print_r($result); // Output: Array ( [0] => A [1] => B [2] => D [3] => E [4] => H [5] => C [6] => F [7] => G )
?>