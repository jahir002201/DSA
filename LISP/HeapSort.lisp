(defun heapify (arr n i)
  "Ensure the subtree rooted at index i is a heap."
  (let* ((largest i)
         (left (+ (* 2 i) 1))
         (right (+ (* 2 i) 2)))
    (when (and (< left n) (> (aref arr left) (aref arr largest)))
      (setf largest left))
    (when (and (< right n) (> (aref arr right) (aref arr largest)))
      (setf largest right))
    (when (/= i largest)
      (rotatef (aref arr i) (aref arr largest))
      (heapify arr n largest))))

(defun heap-sort (arr)
  "Sort an array using the heap sort algorithm."
  (let ((n (length arr)))
    ;; Build a max heap
    (loop for i from (floor (/ n 2)) downto 0 do
      (heapify arr n i))
    ;; Extract elements from the heap one by one
    (loop for i from (1- n) downto 1 do
      (rotatef (aref arr 0) (aref arr i))
      (heapify arr i 0))
    arr))

;; Example usage:
(print (heap-sort (make-array 10 :initial-contents '(3 1 4 1 5 9 2 6 5 3))))
