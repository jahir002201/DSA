(defun factorial (n)
  (if (zerop n)
      1
      (* n (factorial (1- n)))))

(format t "Factorial of 5 is: ~A~%" (factorial 5))
