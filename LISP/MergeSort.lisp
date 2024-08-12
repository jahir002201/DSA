(defun my-merge (left right)
  (cond
    ((null left) right)
    ((null right) left)
    ((< (car left) (car right)) (cons (car left) (my-merge (cdr left) right)))
    (t (cons (car right) (my-merge left (cdr right))))))

(defun merge-sort (list)
  (if (or (null list) (null (cdr list)))
      list
      (let* ((middle (floor (/ (length list) 2)))
             (left (subseq list 0 middle))
             (right (subseq list middle)))
        (my-merge (merge-sort left) (merge-sort right)))))

;; Example usage:
(print (merge-sort '(3 1 4 1 5 9 2 6 5 3 5)))
