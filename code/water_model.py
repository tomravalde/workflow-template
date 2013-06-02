from coopr.pyomo import *

model = AbstractModel()

# Declare the sets
model.R = Set()
model.P = Set()
model.Q = Set()

# Declare the parameters
model.resource_quality = Param(model.R, model.Q, initialize=0)
model.prod_coeff = Param(model.P, model.R, model.Q, initialize=0)
model.demand_quality = Param(model.R, model.Q, initialize=0)
model.demand_quantity = Param(model.R, initialize=0)
model.cost = Param(model.R, model.Q, initialize=0)
model.qual_coeff = Param(model.P, model.R, model.Q, initialize=0)
model.cheat = Param(model.R, model.Q, initialize=0)

# Declare the variables
model.imports = Var(model.R, bounds=(0, None))
model.prod_rate = Var(model.P, within=Reals)
model.production = Var(model.P, model.R, model.Q, within=Reals)
model.production_quantity = Var(model.P, model.R, within=Reals)
model.export = Var(model.R, bounds=(0, None))
model.Z = Var()

# Declare the equations
def prod_quantity(model, p, r ,q):
    if (model.qual_coeff[p,r,q] != 1):
        return Constraint.Skip
    else:
        return (model.production_quantity[p,r]*model.resource_quality[r,q] - model.production[p,r,q]*model.cheat[r,q] == 0)

def resource_production(model, p, r, q):
    return model.production[p,r,q] == model.prod_rate[p]*model.prod_coeff[p,r,q]

def quality_balance(model, q):
    return sum((model.resource_quality[r,q]*model.imports[r] + 
                sum((model.production[p, r, q]) for p in model.P) - 
                model.demand_quality[r,q] - 
                model.resource_quality[r,q]*model.export[r]) for r in model.R) == 0

def quantity_balance(model, r):
    return (model.imports[r] + 
            sum((model.production_quantity[p,r]) for p in model.P) - 
            model.demand_quantity[r] - 
            model.export[r] == 0)

model.quality = Constraint(model.Q, rule=quality_balance)
model.quantity = Constraint(model.R, rule=quantity_balance)
model.prod = Constraint(model.P, model.R, model.Q, rule=resource_production)
model.prodq = Constraint(model.P, model.R, model.Q, rule=prod_quantity)

# Declare the objective
def obj_rule(model):
    return sum((sum((model.cost[r,q]*model.resource_quality[r,q]*model.imports[r]) for r in model.R)) for q in model.Q)

model.obj = Objective(rule=obj_rule, sense=minimize)


