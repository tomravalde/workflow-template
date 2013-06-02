from coopr.pyomo import *

model = AbstractModel()

# Declare the sets
model.R = Set()
model.P = Set()
model.E = Set()
model.imports_bounds = Set() # only some resources have bounds on imports
model.B = Set()
model.NB = Set()

# Declare the parameters
model.imports_min = Param(model.R, initialize=0)
model.imports_max = Param(model.R, initialize=0)
model.demand = Param(model.R, initialize=0)
model.cost_resource = Param(model.R, initialize=0)
model.prod_coeff = Param(model.R, model.P, initialize=0)
model.process_number_min = Param(model.P)
model.process_number_max = Param(model.P)
model.process_rate = Param(model.P)
model.processEmissions = Param(model.P, initialize=0)

# Declare the variables
def import_bounds(model, r):
	return (model.imports_min[r], model.imports_max[r])

def process_number_bounds(model, p):
	return (model.process_number_min[p], model.process_number_max[p])

model.imports = Var(model.R, bounds=import_bounds)
model.exports = Var(model.R, bounds=(0,None))
model.process_number = Var(model.P, bounds=process_number_bounds)

# Declare the equations

def resource_balance(model, r):
	return model.imports[r] + sum((model.prod_coeff[r,p]*model.process_rate[p]*model.process_number[p]) for p in model.P) == model.demand[r] + model.exports[r]

def emissions_limits(model):
	return sum((model.processEmissions[p]*model.process_rate[p]*model.process_number[p]) for p in model.P) <= 1000000000000

#def con_rule_Ifix(model, j):
#	return model.I[j] == model.I_fix[j]

model.constraint_quantity = Constraint(model.R, rule=resource_balance)
model.constraint_emissions = Constraint(rule=emissions_limits)
#model.con_Ifix = Constraint(model.Ifix, rule=con_rule_Ifix)

# Declare the objective
def obj_rule(model):
	return sum((model.cost_resource[r]*model.imports[r]) for r in model.R)

model.obj = Objective(rule=obj_rule)
