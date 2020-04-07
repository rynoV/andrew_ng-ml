function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta.
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %

    % Calculate theta_1 * X_1 + theta_2 * X_2 + ... using column-wise summation.
  predictions = sum(X .* theta', 2);
   % Calculate the differences between the expected values and the actual values
  differences = predictions-y;
  % Calculate the derivative of the error function and apply alpha for each feature
  change_in_theta = alpha * (1/m) * sum(X .* differences);
  % Update each theta with its repective change
  theta = theta .- change_in_theta';

    % ============================================================

    % Save the cost J in every iteration
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
