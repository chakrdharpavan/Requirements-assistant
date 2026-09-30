Problem Statement:- 

A significant number of companies were logging in to our application and utilizing our features for the first time. Moving forward after a month the companies were drooping and not thoroughly using our product.


Hypothesis:-

Is a new competitor there in the market?
I believe that there are few issues in User interface
Is our users satisfied with our product
After creating multiple projects, how does our UI work?
What kind of companies are mostly working with our product

Validation:-

Generate a metrics for daily active users
Generate a metrics for different companies, I mean weather it is SAAS domain, Medical, Pharma etc
Check the defect trends, revise all the tickets, notice are there any bugs that are still there in the UI after user creating multiple projects.
Check whether there is a new competitor in the market, if yes go through their UI, features, offerings and pricings
Conduct customer surveys
Conduct User interviews
Get feedback from customers before leaving the application

Findings:- 

After checking the usage data and talking to a few customers, I found that the product started becoming slow when customers created multiple projects. Some users were also getting stuck on the loading screen, which could be one of the reasons they stopped using the product regularly.

Root cause analysis:-

What kind of features are not working after creating multiple projects
What are customer facing issues
If a user creates five projects does our UI support it?
Which specific screens/features become slow?
UI  automatically spinning if user generates above 9 projects
Are customers unable to complete important workflows because of this issue?

Root Cause:- 

After checking the user behaviour, application performance and customer feedback, I found that the UI was becoming slow when customers created multiple projects. In some cases, the application kept loading and users were unable to complete their tasks. This could be one of the main reasons why customers were not continuing to use the product.

Solution:-

Fix the UI and performance issues that occur when customers create multiple projects. 
Deploy the changes to the development environment. 
Release the fix after confirming that customers can manage multiple projects without performance issues. 
Monitor performance, errors, and usage before rolling it out to everyone.

Enhancement:-

Add an ability, after completing the projects users can delete old data and preserve that data into the cloud for one month.
Before deleting their old data in our cloud send an email,  saying that we are deleting your old data.




Prioritization:-

Rank      Feature                            Reason                            Impact        Effort

P1        Fix UI/performance issues    Directly affects customers              High          2days
P2        Enhancement                  Helps customers manage older projects   Medium        1day
P3        Email notification          Keeps customers informed before deleting Low           0.5day




Experiment/Rollout:-

Deploy these changes for only single division
The remaining customers shall use our old version 
Compare performance, usage and error rates between both groups.
If the new version performs better without introducing new issues, gradually roll it out to the remaining customers.



Success Metrics:-

Metrics                              Targets

30-day Customer Retention          Increase by 10%
Project Feature Usage              Increase by 15%
UI Loading Time                    Reduce by at least 30%
Error Rate                         Reduce by 20%
Customer Feedback                  Improve after the fix





