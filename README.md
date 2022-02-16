# PP3 - Pay Calculator

Pay Calculator is tool created for an imagined real-world scenario where an owner of a large barn rents space to various dealers. The owner of this land takes a 5% commission from all sales made by the dealers. The problem for the owner is they do not have a central till or payment system yet. So the sales for each dealer come in many different ways such as: scraps of paper or by text, etc. The owner has requested a simple command line programme that will allow them to quickly input sales data for each dealer, and then calculate how much the dealer should be paid and how much should go to the owner of the land.

Pay Calculator achieves the project goal by requesting the data in a command interface on a platform called Heroku, validates the data, calculates the pay for the dealer and the owner, displays it in real-time to the command interface and also then stores it in a Google Sheet for the owner to access historical inputs.

[The live project can be viewed here.](https://pp3-pay-calculator.herokuapp.com/)

![](docs/images/ismysiteresponsive-screenshot.png)

## Planning

I started out my planning the requirements for the Pay Calculator in a flow diagram using [Lucid Charts](https://www.lucidchart.com/pages/). This allowed me to fully scope what I needed the tool to do and was useful to refer back to, to ensure I was staying on track with the intended outputs for the project.

Please see my original plan below:

![](docs/images/plan-flow-diagram.png)

I largely stuck to the plan except I decided to update the worksheet all in one API call rather than on two separate calls to update sales as they were entered and then dealer and owner pay at the end once calculated. I read that it is best served to have as few API calls as possible in an application to keep loading/run-time as quick as possible.

## How to use Pay Calculator

There are currently 4 imaginary dealers in the Google Sheet used for this project. You will need a Dealer_ID from the picture below to make the tool work.

![](docs/images/dealer-screenshot.png)

1. Enter your Dealer_ID into the command line prompt, taking note of type of data the tool will accept.
2. Enter the sales total for that dealer into the command line, again taking note of the type of data the tool will accept.

The outcome of a successful use of the tool will be a display of the total to pay to the dealer and the total to pay to the house (owner). The command line interface will also confirm data has been added to the Google worksheet.

## Existing Features


