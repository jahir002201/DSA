(defun bfs (graph start goal)
  (let ((visited (make-hash-table :test #'equal))
        (queue (list start)))
    (loop while queue do
      (let ((node (pop queue)))
        (when (not (gethash node visited))
          (setf (gethash node visited) t)
          (if (equal node goal)
              (return-from bfs t))
          (push (remove-if-not
                 #'(lambda (n) (not (gethash n visited)))
                 (cdr (assoc node graph))) queue))))))
          
;; Example usage:
(let ((graph '((A (B C))
               (B (A D E))
               (C (A F))
               (D (B))
               (E (B F))
               (F (C E)))))
  (print (bfs graph 'A 'F)))  ;; Should print T (true)
