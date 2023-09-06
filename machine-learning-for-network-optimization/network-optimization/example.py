import pulp

# Create a Linear Programming problem
prob = pulp.LpProblem("Bandwidth_Optimization", pulp.LpMaximize)

# Define variables for bandwidth allocation
# Variables represent how much bandwidth to allocate to each application
app1_bw = pulp.LpVariable("App1_Bandwidth", lowBound=0, upBound=None, cat='Continuous')
app2_bw = pulp.LpVariable("App2_Bandwidth", lowBound=0, upBound=None, cat='Continuous')
app3_bw = pulp.LpVariable("App3_Bandwidth", lowBound=0, upBound=None, cat='Continuous')

# Objective function: Maximize total bandwidth utilization
prob += app1_bw + app2_bw + app3_bw, "Total_Bandwidth_Utilization"

# Constraints: Bandwidth limits for each application
prob += app1_bw <= 50, "App1_Bandwidth_Limit"
prob += app2_bw <= 30, "App2_Bandwidth_Limit"
prob += app3_bw <= 40, "App3_Bandwidth_Limit"

# Solve the linear programming problem
prob.solve()

# Print the optimization status
print("Status:", pulp.LpStatus[prob.status])

# Print the optimized bandwidth allocation
print("Optimized Bandwidth Allocation:")
print("App1 Bandwidth:", app1_bw.varValue)
print("App2 Bandwidth:", app2_bw.varValue)
print("App3 Bandwidth:", app3_bw.varValue)
