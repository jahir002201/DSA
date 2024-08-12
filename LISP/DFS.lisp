(defun dfs (graph start goal)
  (let ((visited (make-hash-table :test #'equal))
        (stack (list start)))
    (loop while stack do
      (let ((node (pop stack)))
        (unless (gethash node visited)
          (setf (gethash node visited) t)
          (if (equal node goal)
              (return-from dfs t))
          (push (remove-if-not
                 #'(lambda (n) (not (gethash n visited)))
                 (cdr (assoc node graph))) stack))))))
        
(defun run-dfs-example ()
  (let ((graph '((A (B C))
                 (B (A D E))
                 (C (A F))
                 (D (B))
                 (E (B F))
                 (F (C E)))))
    (let ((result (dfs graph 'A 'F)))
      (print (format nil "DFS result: ~A" result)))))

(run-dfs-example)