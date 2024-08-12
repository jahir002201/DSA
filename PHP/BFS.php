<?php
function bfs($graph, $start) {
    $visited = [];
    $queue = [$start]; // Initialize queue with the starting node

    while (!empty($queue)) {
        $node = array_shift($queue); // Dequeue a vertex from queue
        if (!in_array($node, $visited)) {
            $visited[] = $node; // Mark the node as visited

            // Enqueue all adjacent vertices that have not been visited
            foreach ($graph[$node] as $neighbor) {
                if (!in_array($neighbor, $visited)) {
                    $queue[] = $neighbor;
                }
            }
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

$result = bfs($graph, 'A');
print_r($result); // Output: Array ( [0] => A [1] => B [2] => C [3] => D [4] => E [5] => F [6] => G [7] => H )
?>