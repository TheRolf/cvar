param H;
param F;
param S;
param T;

set Hedg := 1..H;
set Forw := 1..F;
set Scen := 1..S;
set Time := T+1..H;

param alpha;
param epsilon;

param D{Hedg};
param A{Forw, Hedg};
param P0{Forw};
param y{Scen, Hedg};

var x{Forw};
var u{Scen} >= 0;
var L;

minimize risk: L + 1/((1-alpha)*S) * sum{s in Scen} u[s];

subject to positivepart{s in Scen}:
	( sum{t in Time} (1-0.15*(sum{f in Forw} A[f,t]*x[f] - D[t])) *y[s,t] * (sum{f in Forw} A[f,t]*x[f] - D[t]) ) - ( sum{f in Forw} (1+epsilon*x[f])*P0[f]*x[f] ) + L + u[s] >= 0;
