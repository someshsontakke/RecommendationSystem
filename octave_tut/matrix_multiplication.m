% Unvectorized implementation of matrix_multiplication

prediction = 0.0;
for j = 1:n+1,
	prediction = prediction + theta(j)*x(j)
end;

% Vectorized implementation

prediction = theta' *x;
