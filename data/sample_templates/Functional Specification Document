Online Pharmacy Management System 

The functional requirement document defines the functional behaviour of the online pharmacy management system it is prepared based on the approved business requirement document. 
It is intended for developers, QA team, project managers and product teams. The document covers user requirements, functional requirements and error handling

System Overview:-

This Online Pharmacy Management System includes dashboard, user registration & login and tracking etc. 
It supports six roles Customers, Pharmacist, Delivery, Agent Admin, IT Department and Payment Gateway 

FR1:-

Feature Name:- User Login & Registration

Who uses it:- it is used by customers

Inputs:- 

User can register with their email ids
User can create a new password while registering
User can login with their email & passwords
User can change their password while logging in

Behavior:- 

When user logged in they should enter in to homepage
User can change their password while logging in

Validations:-
- Email must be in valid format (contains @ and domain)
- Password must be minimum 8 characters
- System shall reject login after 5 failed attempts


Success outcome:-
User is redirected to dashboard within 2 seconds of valid login

Failure outcome:-
System displays "Invalid email or password" and does not redirect 


FR2:- 

Feature Name:- Product Grid

Who uses it:- it is used by customers

Inputs:- 

User can see all the medicines information in Product Grid
In fact they can search their medicines on the UI
User can check their profile on the dashboard

Behaviour

Whenever user clicks on any medicine it should open another page and showcase full details of the medicines
A search button should be developed on the UI where user can search for medicines

Validations:- 
Search should only return medicines that match the entered name or category
If no matching medicine is found, system shall display, No medicines found for this search
Search field shall not accept special characters like @, #, %

Success outcome:-
Search results are displayed within 1-2 seconds of the user entering a valid medicine name

Failure outcome:-
System displays "No medicines found" and prompts user to try a different search term




FR3:- Tracking

A tracking system should be enabled on the UI
Where customers can see their order tracking
Admin department can check delivery agent status

Validations:-
Tracking status shall update only after the order is confirmed
If delivery agent location is not available, last known status should be shown

Success outcome:-
Customer and admin can view real-time order status without page refresh

Failure outcome:-
System displays "Tracking information not available right now, please check after some time"

FR4:- Inventory Management

An inventory management system should be enabled
It should be visible for management only
The UI displays manage stores, generate reports, handle complaints

Validations:-
Only admin and management roles shall have access to this section
Stock count cannot be a negative number

Success outcome:-
Reports and stock details load correctly for authorised users only

Failure outcome:-
System displays "You do not have permission to access this page" for unauthorised users


NFR1:-  The ui should work on website, Android &  IOS
NFR2:-  The system can handle concurrent of 500 users
NFR3:-  The system shall work on all the relevant browsers
NFR4:-  The system passwords shall be encrypted
NFR5:-  The system shall maintain 99.9% uptime given the critical nature of medicine availability for customers
NFR6:- The application should provide a simple and accessible interface that can be used across supported devices and screen sizes.


Error Handling:-

If user trying to login with another details an error message should be displayed
If customer didn’t pay the amount and trying to order, an error message should be displayed
If customer upload invalid prescription an error message should be displayed
While paying amount if customer didn’t enter valid amount and try to proceed an error message should be displayed
While the product is in cart and user visited after days and item is out of stock an error message should be displayed


Business Rules:-

User must be logged in 
User can buy products if they are in stock
Online Delivery will be applicable for certain region
An email is mandatory while logged in otherwise they can’t logged in
Customer can pay only through UPI/Card
