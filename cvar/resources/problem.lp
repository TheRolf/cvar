\* Source Pyomo model name=unknown *\

min 
Risk:
+1 L_var
+1.2500000000000002 u_vars(1)
+1.2500000000000002 u_vars(2)
+1.2500000000000002 u_vars(3)
+1.2500000000000002 u_vars(4)

s.t.

c_l_PositivePartConstraint(1)_:
+1 L_var
+1 u_vars(1)
+214 x_vars(1)
+90.200000000000045 x_vars(2)
+123.79999999999995 x_vars(3)
+ [
-4.5 x_vars(3) ^ 2
-4.5 x_vars(2) ^ 2
-9 x_vars(1) ^ 2
]
>= 16611.719999999998

c_l_PositivePartConstraint(2)_:
+1 L_var
+1 u_vars(2)
+159.61000000000013 x_vars(1)
+54.189999999999998 x_vars(2)
+105.41999999999996 x_vars(3)
+ [
-4.5 x_vars(3) ^ 2
-4.5 x_vars(2) ^ 2
-9 x_vars(1) ^ 2
]
>= 15812.569999999998

c_l_PositivePartConstraint(3)_:
+1 L_var
+1 u_vars(3)
+197.06999999999994 x_vars(1)
+47.080000000000041 x_vars(2)
+149.99000000000001 x_vars(3)
+ [
-4.5 x_vars(3) ^ 2
-4.5 x_vars(2) ^ 2
-9 x_vars(1) ^ 2
]
>= 16737.82

c_l_PositivePartConstraint(4)_:
+1 L_var
+1 u_vars(4)
+183.98000000000025 x_vars(1)
+33.849999999999966 x_vars(2)
+150.13000000000011 x_vars(3)
+ [
-4.5 x_vars(3) ^ 2
-4.5 x_vars(2) ^ 2
-9 x_vars(1) ^ 2
]
>= 16530.929999999997

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds 
    -inf <= x_vars(1) <= +inf
    -inf <= x_vars(2) <= +inf
    -inf <= x_vars(3) <= +inf
   0 <= u_vars(1) <= +inf
   0 <= u_vars(2) <= +inf
   0 <= u_vars(3) <= +inf
   0 <= u_vars(4) <= +inf
    -inf <= L_var <= +inf
end 
