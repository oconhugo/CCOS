# Cashier-Chef Ordering System (CCOS)
Repository for CCOS

## Introduction
The system provides a method of ordering on a restaurant, where the client goes to the cashier and orders his food. The cashier selects the food ordered by the customer and is sent to the chef. The chef will have a PC displaying a list of the orders. The chef will then be able to click/touch on any order number to display the content and selects it as complete to dissapear from the list.

## Demostration
https://www.youtube.com/watch?v=XUbXtwzE9M8 

Cashier:<br/><br/>
<img src = "Images/Capture.PNG" width = "800" style = "margin-left:auto;margin-right:auto;" > <br/><br/>
Chef: <br/><br/>
<img src = "Images/Capture1.PNG" width = "800">

## Technologies
### Languages
-Python 3
### Libraries
-EasyTkinter 1.1.0<br/>
-PyInstaller 3.6<br/>
-XlsxWriter 1.2.8<br/>
-future 0.18.2<br/>
-openyxl 3.0.3<br/>
-threadsafe-tkinter 1.0.2<br/>

## Prerequisites
The following software is needed to install and run the system:<br/>
		-Python 2.7 or higher<br/>
		
The following hardware is needed to install and run the system:<br/>
		-Two PCs running in a same network<br/>
    
## Installation
To install the system just download the files and make sure that the two computer that are running the system are on the same network.

## Deployment
Before turning the system on the PCs, we need to make sure that the PCs are connected in the same network and that sockets can communicate.

First,on the chef PC, go to the chef.py program and change the IP to the IP of the chef computer. Then,on the cashier PC, go to client.py and change the IP to the IP of the chef computer.

Now, go to the file explorer on both PC and click on network on the left sidebar. The computers of the system needs to appear on the window, showing they are in the same network. 

After that, open the command window and type the following:

On cashier: ping *Chef PC IP address* - It need to show a connection was made succesfully
On chef: ping *Cashier PC IP addess*  - It need to show a connection was made succesfully

Then, open Windows Defender Firewall Advanced Security. On the left panel of the window, click on Inbound rules. Create a new rule by clicking on New Rule on the right panel of the window.
Click on port on the new window that pops up. Select TCP rule and type in the specific port you are going to use to connect between the PCs 
(You can select the port by going to the chef.py and server.py files anf change it, it needs to be >1024). Click on next until a Name text box appears and put
any desired name for the rule. Then click finished. Do this firewall step for both PCs. You can now run the system.

To run the system, the chef.py need to be ran first, as it is the server for the sockets, then cashier need to be run to connect to the server. 

## Launch
Go to the project folder. First run the chef, as it is going to be the socket server, and after that run the cashier, which is the client socket.

## Description
### Context
This started as a personal project to provide a system for a mexican taqueria. We got contacted by the owner of a mexican restaurant, asking us for a system that optimized his ordering restaurant procedure.The main problem with his process was that taking the order, sending the order to the cooker, and deliver the food was done manually. As consecuence, this make the ordering process and delivery slower.<br/>
In response to this issues, we created the "Cashier-chef Ordering System" for the restaurant. That will optimize the process by providing an interface for the cashier and the cooker where will keep comunication, receive orders faster, and complete it quickler as well. This increses the sales and produce more income for the restaurant. This system also create an excel file that stores the total sales and earning making the cashier life easier.
		
### What can the project specifically do
The system gets the order from the cashier and sents it to the chef. The chef then obtains the order an it is added to a list. The chef sees his specific
interface on a PC, which contains a list of the orders on the left side, and on the right side the content of the order he clicks. Every order that is
completed on the day, every day, gets stored in an excel file. Each excel file has the orders of the days and its title is the date the orders were taken. The files
also show the total orders and sales of each day. All the files are stored in a folder called Inventory that is created inside the priject folder.

### Features
#### Cashier
-Items can be selected from the menu by clicking on the buttons on its interface.<br/>
-Text boxes to choose total cost for certain special Items.<br/>
-Select if the order is to go by clicking on a checkbox.<br/>
-See the total cost of the order on its interface. The button see total needs to be clicked before sentind the order.<br/>
-Interface will reset automatically after sending the order to the chef.<br/>
-The order individual items and cost will be displayed when selected on the cashiers interface.<br/>
-The order can be cancelled at any time before sending it to the chef.<br/>
-Send a note to the chef along with the order.<br/>
#### Chef
-See a list of uncompleted orders.<br/>
-Ability to toggle thru the orders to see its content, by clicking on the order number.<br/>
-Select an order as completed, which would eliminate it from the list.<br/>
#### Others
-A inventory folder is created inside the project folder, if it is not already created.<br/>
-An excel file is generated per day, in which every order is stored, along with the total orders per day and total sales.<br/>
	
### Links
Demo Link: 

## Usage
This system can be used in any restaurant where the order is taken by a cashier. This particular code was made with a menu for a Mexican restaurant, but it can easily be modified to fit the menu of any restaurant.

## Support
For any questions, do not hesistate to contact the authors.

## Roadmap
In the future, we will connect the system to a ticket machine and print a ticket for the client. This will happen when the system is implemented on a restaurant.

## Authors and Acknowledgements
Hugo Ocon - oconhugo14@gmail.com <br/>
Alejandro Ibarra Polanco - alejandro.ibarra.p@gmail.com  

## Project Status
Complete
