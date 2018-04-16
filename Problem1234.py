import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# simulating no therapy
# create a cohort
cohort_no = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_no = cohort_no.simulate()

# simulating anticoagulation therapy
# create a cohort
cohort_ANTICOAG = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_ANTICOAG = cohort_ANTICOAG.simulate()


#Problem1: Use your simulation model to estimate the discounted total cost and discounted total utility of patients
#who start in the state “Well” for both treatment scenarios. You can assume that the discount rate is 3%.

# print the estimates for the mean survival time and mean times of stroke, mean discounted total cost and utility

print("Problem 1")
SupportMarkov.print_outcomes(simOutputs_no, "No Drug:")
SupportMarkov.print_outcomes(simOutputs_ANTICOAG, "Anticoagulation:")

# Problem 2: Change in Outcomes (Weight 1): Estimate the change in the expected discounted cost,
# the expected discounted utility, and the expected number of strokes when the anticoagulation drug is used.
# Report the 95% confidence intervals for all your estimates.

# print comparative outcomes
print("Problem 2")
SupportMarkov.print_comparative_outcomes(simOutputs_no, simOutputs_ANTICOAG)

# Problem 3: Cost-Utility Analysis (Weight 1): Use a cost-utility plane to display
# the expected discounted incremental utility and cost form the anticoagulation drug.
# Report the results of your cost-utility analysis in a table.
# Make sure to include the 95% confidence intervals for all reported estimates
# (discounted cost, discounted utility, incremental discounted cost, incremental discounted utility and the ICER).

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_no, simOutputs_ANTICOAG)

# Problem 4: Cost-Benefit Analysis (Weight 1): Plot the incremental net monetary benefit curve
# when the anticoagulation drugs is used for varying values of willingness-to-pay.
# Show the 95% confidence region. At what level of willingness-to-pay would you recommend
# adopting this anticoagulation drug?

print("As shown in the graph, I would recommend the anticoagulation drug when the WTP value is around 22,000.")